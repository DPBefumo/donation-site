from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import stripe

stripe.api_key = "sk_test_51HYwLhDLxlZyq8nYi9BQxltfiOsLZy8m8f4tmtCPouAxkNB5Uh0NT3EAYPS6PyO1z2K0yxuMBhg2IdRzlcPt0E9K00OdCqRqzd"

def index(request):
    return render(request, 'core/index.html')


def donate(request):
    
    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email = request.POST['email'],
            name = request.POST['name'],
            source = request.POST['stripeToken']
        )
        charge = stripe.Charge.create(
            customer = customer,
            amount = amount*100,
            currency = 'usd',
            description = 'Donation'
        )
    return redirect(reverse('success', args=[amount]))


def successPage(request, args):
    amount = args
    return render(request, 'core/success.html', {'amount':amount})


def cardDetail(request):
    pass