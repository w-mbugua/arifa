from django.urls import path
from .views import experts_List

urlpatterns = [ 
    path('<slug:market_name>/', experts_List, name='market_experts'),
]