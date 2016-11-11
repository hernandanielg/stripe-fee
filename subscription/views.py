from django.shortcuts import render, redirect
from django.views import View
from .forms import SubscriptionForm

class HomeView(View):

    def get(self, request):
        form = SubscriptionForm()
        return render(request, 'subscription/home.html',{'form':form})


class SubscribeView(View):

    def get(self, request):
        return redirect('home')

    def post(self, request):
        form = SubscriptionForm(request.POST or None)

        context = {
            "success": "You've been suscribed!",
            "form": form
        }
        
        return render(request, 'subscription/home.html',context)
