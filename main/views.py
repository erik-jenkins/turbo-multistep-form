from django.shortcuts import redirect, render
from django import forms
import time

def ensure_turbo_frame(redirect_to, **redirect_kwargs):
    def _ensure_turbo_frame(view_func):
        def _wrapped_view_func(request, *args, **kwargs):
            if not request.headers.get('Turbo-Frame'):
                return redirect(redirect_to, **redirect_kwargs)

            return view_func(request, *args, **kwargs)
        return _wrapped_view_func

    return _ensure_turbo_frame


def account(request):
    return render(request, 'main/account.html')


class AccountForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8)


@ensure_turbo_frame(redirect_to='account')
def account_submit(request):
    form = AccountForm(request.POST)
    if not form.is_valid():
        return render(request, 'main/account.html', {'form': form})

    return redirect('address')


@ensure_turbo_frame(redirect_to='account')
def address(request):
    return render(request, 'main/address.html')


class AddressForm(forms.Form):
    address = forms.CharField()
    apt = forms.CharField(required=False)
    city = forms.CharField()
    state = forms.CharField()
    zip = forms.CharField()


@ensure_turbo_frame(redirect_to='account')
def address_submit(request):
    form = AddressForm(request.POST)
    if not form.is_valid():
        return render(request, 'main/address.html', {'form': form})

    return redirect('payment')


@ensure_turbo_frame(redirect_to='account')
def payment(request):
    return render(request, 'main/payment.html')


class PaymentForm(forms.Form):
    card_number = forms.CharField()


def payment_submit(request):
    account_form = AccountForm(request.POST)
    if not account_form.is_valid():
        print('woot')
        return render(request, 'main/account.html', {'form': account_form})

    address_form = AddressForm(request.POST)
    if not address_form.is_valid():
        return render(request, 'main/address.html', {'form': address_form})

    payment_form = PaymentForm(request.POST)
    if not payment_form.is_valid():
        return render(request, 'main/payment.html', {'form': payment_form})

    print('Doing some work to create the account...')

    return render(request, 'main/success.html')
