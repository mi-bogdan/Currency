
from urllib.request import Request
from django.shortcuts import render
from .models import *
import requests


def index(request):
    responce = requests.get(
        url='https://v6.exchangerate-api.com/v6/2fcbf30ca3abbfcbac940c70/latest/RUB').json()
    currencies = responce.get('conversion_rates')
    
    

    if  request.method == "GET":
        context={
            'currency':currencies,

        }
        return render(request, template_name='conversion/conversion.html', context=context)

    if request.method == "POST":
        from_amount=float(request.POST.get('from_amount'))
        from_curr=request.POST.get('from_curr')
        to_curr=request.POST.get('to_curr')
        converted_amount=round(currencies[to_curr]* from_amount,2)

        context={
            'currency':currencies,
            'from_amount':from_amount,
            'from_curr':from_curr,
            'to_curr':to_curr,
            'converted_amount':converted_amount,
        }

        bd={
            'from_amount':from_amount,
            'from_curr':from_curr,
            'to_curr':to_curr,
            'converted_amount':converted_amount,
        }

        Valute.objects.create(**bd)


        return render(request, template_name='conversion/conversion.html', context=context)
        

   
def lists(request):
    context={
        'valutes':Valute.objects.order_by('-data_converted')
    }
    return render(request, template_name='conversion/list.html', context=context)
