from django import forms

class SubscriptionForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    card_number = forms.CharField(max_length=16)
    exp_month = forms.CharField(max_length=2)
    exp_year = forms.CharField(max_length=4)
    cvc = forms.CharField(max_length=3)
