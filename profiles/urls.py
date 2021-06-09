from django.urls import path
from .views import(
    ProfileDetailView,
    ProfileUpdateView,
    ProfileListView,
    ProfileCreateView,
    ask_expert,
    create_profile,
    retrieve_messages,
    MessageView,
    reply_msg,
    CompleteProfileView,
    user_follow
    )

urlpatterns = [ 
    path('follow/', user_follow, name='user_follow'),
    path('<slug:slug>/', ProfileDetailView.as_view(), name='profile'),
    path('<slug:slug>/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('view_profiles/', ProfileListView.as_view(), name='profiles_list'),
    path('professional/details/', CompleteProfileView.as_view(), name='registration2'),
    path('ask_expert/<slug:slug>/', ask_expert, name='ask'),
    path('<slug:slug>/messages/', retrieve_messages, name='dms'),
    path('message/<int:msg_id>/', MessageView, name='message'),
    path('<int:msg_id>/send_reply/', reply_msg, name='reply_msg'),
    
]