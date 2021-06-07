from django.urls import path
from .views import PostDeleteView, PostUpdateView, PostDetailView

urlpatterns = [ 
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]