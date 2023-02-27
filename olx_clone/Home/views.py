from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from . models import *


# Create your views here.

#to show all products added by user
def home_page(request,category_slug=None):
    category_page=None
    products=None
    if category_slug!=None:
        category_page=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.all().filter(category=category_page)
    else:
        products=Product.objects.all()
    context={
        'category':category_page,
        'products':products
    }
    return render(request,'index.html',context)


#function for add product
def sell_product(request):
    categories=Category.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        category_id = request.POST.get('category') #to get category from dropdown
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
