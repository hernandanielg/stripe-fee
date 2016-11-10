from django.shortcuts import render, redirect
from django.views import View
from .models import User

import stripe


class HomeView(View):

    def get(self, request):
        return render(request, 'subscription/home.html')


class SubscribeView(View):

    stripe.api_key = 'sk_test_xJNBke1EQ4YPIrZo81lwTSjo'

    def get(self, request):
        return redirect('home')

    def post(self, request):
        cvc = request.POST['cvc']
        card_number = request.POST['card-number']
        expiration_date = request.POST['expiration-date'].split('-')
        exp_year = expiration_date[0]
        exp_month = expiration_date[1]

        try:
            token = stripe.Token.create(
                card={
                    "number": card_number,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "cvc": cvc
                }
            )
        except stripe.error.CardError as e:
            body = e.json_body
            error = body['error']
            return render(request, 'subscription/home.html', {"error": error['message']})

        name = request.POST['name']
        email = request.POST['email']

        print('pasaba por aquí %s' % token.id);

        try:
            customer = stripe.Customer.create(
                description=name,
                email=email,
                source=token.id
            )
        except Exception as e:
            body = e.json_body
            error = body['error']
            return render(request, 'subscription/home.html',{"error": error['message']})

        print('look how far I am')

        user = User()
        user.name = name
        user.email = email
        user.id_stripe = customer.id
        user.save()

        return render(request, 'subscription/home.html', {"success": "You've been suscribed!"})


