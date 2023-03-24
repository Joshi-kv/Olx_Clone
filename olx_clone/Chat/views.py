from django.shortcuts import render
from Home.models import Product
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='User:login')
def chat(request,):
    return render(request, 'chat.html' )

@login_required(login_url='User:login')
def chat_page(request,product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Exception as e :
        raise e
    
    context={
        'product':product,     
        
    }
    return render(request, 'chat.html',context )