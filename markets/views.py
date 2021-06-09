from django.shortcuts import render
from django.views.generic import ListView
from .models import Market
from profiles.models import Profile

# Create your views here.

def experts_List(request, market_name):
    market = Market.objects.get(slug=market_name)
    experts = market.get_experts()
    print('EXPERTS', experts)
    return render(request, 'markets/experts.html', {"market": market, "experts": experts})


