from django.shortcuts import render
from Home.models import Product
from datetime import datetime
# Create your views here.

now = datetime.now()
day_name = now.strftime('%A')
day = now.day
month = now.strftime('%B')
time =now.time

def chat_page(request,product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Exception as e :
        raise e
    
    context={
        'product':product,
        'day_name' : day_name,
        'day' : day,
        'month' : month,
        'time':time
        
        
    }
    return render(request, 'chat.html',context )
