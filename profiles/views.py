from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, ListView, CreateView
from .models import Profile, Message, Client
from .forms import UserProfileForm, MessageForm, ReplyForm, Registration2Form
from django.contrib.auth.mixins import LoginRequiredMixin
from users.email import send_client_email
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ('bio', 'photo',)
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

class CompleteProfileView(CreateView):
    form_class = Registration2Form
    model = Profile
    template_name = 'profiles/registrarion2.html'


def ask_expert(request, pk):
    form = MessageForm()
    profile = Profile.objects.get(pk=pk)
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

def retrieve_messages(request, pk):
    profile = Profile.objects.get(pk=pk)
    messages = profile.get_messages()
    print("Profile",profile)
    print("Messages",messages)
    return render(request, 'profiles/dms.html', {"messages": messages, "profile": profile})

def MessageView(request, msg_id):
    message = Message.objects.get(pk=msg_id)
    return render(request, 'messages/message_details.html', {"message": message})

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


