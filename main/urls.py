from django.urls import path

from main import views

urlpatterns = [
    path('account', views.account, name='account'),
    path('account/submit', views.account_submit, name='account-submit'),
    path('address', views.address, name='address'),
    path('address/submit', views.address_submit, name='address-submit'),
    path('payment', views.payment, name='payment'),
    path('submit', views.address, name='submit'),
]
