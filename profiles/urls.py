from django.urls import path
from .views import(
    ProfileDetailView,
    ProfileUpdateView,
    ProfileListView,
    ProfileCreateView,
    ask_expert,
    retrieve_messages,
    MessageView,
    reply_msg,
    CompleteProfileView,
    )

urlpatterns = [ 
    path('<slug:slug>/', ProfileDetailView.as_view(), name='profile'),
    path('<int:pk>/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('view_profiles/', ProfileListView.as_view(), name='profiles_list'),
    path('create/', ProfileCreateView.as_view(), name='create_profile'),
    path('professional/details/', CompleteProfileView.as_view(), name='registration2'),
    path('<int:pk>/ask_expert/', ask_expert, name='ask'),
    path('<int:pk>/messages/', retrieve_messages, name='dms'),
    path('message/<int:msg_id>/', MessageView, name='message'),
    path('<int:msg_id>/send_reply/', reply_msg, name='reply_msg'),
]