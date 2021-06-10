from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, ListView, CreateView
from .models import Profile, Message, Client
from .forms import ReviewForm, UserProfileForm, MessageForm, ReplyForm, Registration2Form
from django.contrib.auth.mixins import LoginRequiredMixin
from users.email import send_client_email
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from users.decorators import expert_required


from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Contact
from django.views.decorators.csrf import csrf_exempt


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile

    template_name = 'profiles/profile_detail.html'

    def get_context_data(self, **kwargs):
        kwargs['form'] = ReviewForm()
        return super().get_context_data(**kwargs)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ('bio', 'photo', 'market')
    template_name = 'profiles/profile_edit.html'

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'profiles_list'
    template_name = 'profiles/profiles_list.html'

class ProfileCreateView(LoginRequiredMixin, CreateView):
    form_class = UserProfileForm
    model = Profile
    template_name = 'profiles/profile_reg.html'

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return super().form_valid(form)

@expert_required
def create_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        user = get_user_model().objects.order_by('-id')[:1]
        profile = form.save(commit=False)
        for item in user:
            user = item
        profile.user = user
        profile.save()
        return redirect('home')
    return render(request, 'profiles/profile_reg.html', {"form": form})

class CompleteProfileView(CreateView):
    form_class = Registration2Form
    model = Profile
    template_name = 'profiles/registration2.html'


def ask_expert(request, slug):
    form = MessageForm()
    profile = Profile.objects.get(slug=slug)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            client = Client(name=request.user.username, email=request.user.email, client_of=profile)
            client.save()
            f_rom = client
            to = profile
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            new_message = Message(to=to, subject=subject, message=message, f_rom=f_rom)
            new_message.save()         
            # send_welcome_email(name, expert.user, expert.user.email)
            return redirect('home')

    return render(request, 'profiles/ask.html', {"form": form})

# for both or just the expert?
def retrieve_messages(request, slug):
    profile = Profile.objects.get(slug=slug)
    messages = profile.get_messages()
    print("Profile",profile)
    print("Messages",messages)
    return render(request, 'profiles/dms.html', {"messages": messages, "profile": profile})

def MessageView(request, msg_id):
    form = ReplyForm()
    message = Message.objects.get(pk=msg_id)
    if request.method == 'POST':
        print("RESPONSE FROM EXPERT",request.user.is_expert)
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.sender = request.user
            reply.message = message
            reply.save()
            return redirect('message', message.id)
    return render(request, 'messages/message_details.html', {"message": message, "form": form})

# for both?
def reply_msg(request, msg_id):
    form = ReplyForm()
    message = Message.objects.get(id=msg_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            sender = request.user.email
            name = message.f_rom.name
            receiver = message.f_rom.email
            subject = message.subject
            response = form.cleaned_data['response']
            send_client_email(subject, sender, response, name, receiver)
            send_mail(subject, response, sender, [receiver],fail_silently=False,)
            return redirect('message', message.id)
    return render(request, 'email/reply.html', {"form": form, "message": message})


@require_POST
@csrf_exempt
def user_follow(request):
    profile_id = request.POST.get('id')
    action = request.POST.get('action')
    profile = Profile.objects.get(id=profile_id)
    if profile_id and action:
        try:
            to_follow = profile
            followr = request.user
            print(f"{followr} WANTS TO FOLLOW {to_follow}")
            if action == 'follow':
                profile.followers.add(followr)
            else:
                profile.followers.remove(followr)
            return JsonResponse({"status": "ok"})
        except get_user_model().DoesNotExist:
            return JsonResponse({"status": "error"})
    return JsonResponse({"status": "error"})

def review(request, slug):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            print("IT IS VALID")
            review = form.save(commit=False)
            review.user = request.user
            profile = Profile.objects.get(slug=slug)
            review.reviewed = profile
            review.save()
            print("REVIEW",review.user, review.reviewed)
            return redirect('profile', slug)
    return render(request, 'profiles/review.html', {"form": form})

def show_followers(request, slug):
    profile = Profile.objects.get(slug=slug)
    profile_followers = profile.followers.all()
    print("FOLLOWERS",profile_followers)
    return render(request, 'profiles/followers.html', {"profile_followers": profile_followers})

def client_messages(request):
    user = request.user
    messages = Message.objects.filter(f_rom=user).all()
    return render(request, 'messages/client_messages.html', {"messages": messages})

def search_profile(request):
    search_term = request.GET.get('searchword')
    results = Profile.search_profile(search_term)
    return render(request, 'profiles/search.html', {"results": results, "term": search_term})



