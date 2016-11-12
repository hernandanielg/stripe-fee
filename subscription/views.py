from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from .forms import SubscriptionForm
from .models import User,Payment

import stripe

class HomeView(View):
    def get(self, request):
        return render(request, 'subscription/home.html',{'form': SubscriptionForm()})

class SubscribeView(View):

    stripe.api_key = settings.STRIPE_API_KEY

    def post(self, request):

        form = SubscriptionForm(request.POST or None)

        if not form.is_valid():
            return render(request, 'subscription/home.html',{'form': SubscriptionForm()})

        name = form.cleaned_data['name']
        email = form.cleaned_data['email']

        if User.is_registered(email):
            self.error_message = 'This email is already taken'
            return self.render_with_error(request)

        card = self.create_card_from_form(form)
        token = self.create_token(card)

        if not token:
            return self.render_with_error(request)

        customer = self.create_user(name,email,token)

        if not customer:
            return self.render_with_error(request)

        subscription = self.subscribe_customer_to_plan(customer)

        if not subscription:
            return self.render_with_error(request)

        user = User()
        user.name = name
        user.email = email
        user.id_stripe = customer.id
        user.save()

        plan = stripe.Plan.retrieve(settings.STRIPE_PLAN_ID)

        payment = Payment()
        payment.user = user
        payment.amount = plan.amount
        payment.save()

        return render(request, 'subscription/home.html',{
            'error': False,
            'message': 'You\'ve been subscribed to our plan! ;)',
            "form": SubscriptionForm()
        })

    def create_token(self,card):
        try:
            token = stripe.Token.create(card=card)
            return token
        except stripe.error.CardError as e:
            error = e.json_body['error']
            self.error_message = error['message']

    def create_card_from_form(self,form):
        return {
            "number": form.cleaned_data['card_number'],
            "exp_month": form.cleaned_data['exp_month'],
            "exp_year": form.cleaned_data['exp_year'],
            "cvc": form.cleaned_data['cvc']
        }

    def create_user(self,name,email,token):
        try:
            customer = stripe.Customer.create(
                description = name,
                email = email,
                source = token.id
            )
            return customer
        except stripe.error.StripeError as e:
            error = e.json_body['error']
            self.error_message = error['message']

    def subscribe_customer_to_plan(self,customer):
        try:
            subscription = stripe.Subscription.create(
              customer=customer.id,
              plan=settings.STRIPE_PLAN_ID
            )
            return subscription
        except stripe.error.StripeError as e:
            error = e.json_body['error']
            self.error_message = error['message']

    def render_with_error(self,request):
        context = {
            'error': True,
            'message': self.error_message,
            'form': SubscriptionForm()
        }
        return render(request, 'subscription/home.html',context)
