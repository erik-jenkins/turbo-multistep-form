from django.shortcuts import redirect, render
from django import forms

def account(request):
    return render(request, 'main/account.html')


class AccountForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8)


def account_submit(request):
    form = AccountForm(request.POST)
    if not form.is_valid():
        return render(request, 'main/account.html', {'form': form})

    return redirect('address')


def address(request):
    return render(request, 'main/address.html')


class AddressForm(forms.Form):
    address = forms.CharField()
    apt = forms.CharField(required=False)
    city = forms.CharField()
    state = forms.CharField()
    zip = forms.CharField()


def address_submit(request):
    form = AddressForm(request.POST)
    if not form.is_valid():
        return render(request, 'main/address.html', {'form': form})

    return redirect('payment')


def payment(request):
    return render(request, 'main/payment.html')


def submit(request):
    pass
