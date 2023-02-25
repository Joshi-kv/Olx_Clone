from django.shortcuts import render
from . models import *
# Create your views here.
def home_page(request):
    category=Category.objects.all()
    context={
        'category':category
    }
    return render(request,'index.html',context)

#function for add product
def sell_product(request):
    categories=Category.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        price=request.POST.get('price')
        location=request.POST.get('location')
        model=request.POST.get('model')
        owner_name=request.POST.get('owner_name')
        phone_no=request.POST.get('phone_no')
        description=request.POST.get('description')
        image=request.FILES['image']
        product=Product(name=name,category=category,price=price,location=location,model=model,owner_name=owner_name,phone_no=phone_no,description=description,image=image)
        product.save()
    context={
        'categories':categories
    }
    return render(request,'sell.html',context)
