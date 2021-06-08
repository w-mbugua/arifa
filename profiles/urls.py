from django.urls import path
from .views import(
    ProfileDetailView,
    ProfileUpdateView,
    ProfileListView,
    ProfileCreateView
    )

urlpatterns = [ 
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('<int:pk>/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('view_profiles/', ProfileListView.as_view(), name='profiles_list'),
    path('create/', ProfileCreateView.as_view(), name='create_profile')
]