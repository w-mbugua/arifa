from django.urls import path
from .views import PostDeleteView, PostUpdateView, PostDetailView, create_post, post_like, interesing_news

urlpatterns = [ 
    path('like/', post_like, name='like'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_details'),
    path('add_post/', create_post, name='add_post'),
    path('<str:interest>/news/', interesing_news, name="interesting_news")
]