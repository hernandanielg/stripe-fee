from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from .models import User
import stripe

stripe.api_key = 'sk_test_xJNBke1EQ4YPIrZo81lwTSjo'

class HomeView(View):
    def get(self,request):
        return render(request,'subscription/home.html')

def subscribe(request):
    name = request.POST['name']
    email = request.POST['email']
    card_number = request.POST['card-number']
    expiration_date = request.POST['expiration-date'].split('-')
    exp_year = expiration_date[0]
    exp_month = expiration_date[1]
    cvc = request.POST['cvc']

    data = {}
    data['name'] = name
    data['email'] = email
    data['card-number'] = card_number
    data['exp_month'] = exp_month
    data['exp_year'] = exp_year
    data['cvc'] = cvc

    return JsonResponse(data)

