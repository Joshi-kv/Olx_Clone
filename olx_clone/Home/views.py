from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from . models import *
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

#to show all products added by user
def home_page(request, category_slug=None):
    current_user = request.user
    category_page = None
    products = None

    if category_slug:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category_page).exclude(owner_name=current_user)
    else:
        products = Product.objects.exclude(owner_name=current_user)

    context = {
        'category': category_page,
        'products': products
    }
    return render(request, 'index.html', context)


#to display items added by user
def my_adds(request):
    current_user = request.user
    products = Product.objects.filter(owner_name=current_user)

    context = {
        'products': products
    }
    return render(request, 'myadds.html', context)

#to remove added items
def remove_adds(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            data = {'success': True}
        except Product.DoesNotExist:
            data = {'success': False, 'error': 'Product does not exist or you do not have permission to delete it.'}
    else:
        data = {'success': False, 'error': 'Invalid request method.'}

    return JsonResponse(data)


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
    return render(request,'sellproduct.html',context)

#function to view product details
def product_details(request,category_slug,product_id):
    try:
        products=Product.objects.get(category__slug=category_slug,id=product_id)
    except Exception as e:
        raise e
    is_owner = (products.owner_name == request.user)
    context={
        'products':products,
        'is_owner':is_owner
    }
    return render(request,'product.html',context)

def search(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(location__icontains=query)|Q(name__icontains=query)|Q(description__icontains=query)|Q(category__name__icontains=query))
        
    context={
        'query':query,
        'products':products,
    
    }
    return render(request,'search.html',context)

#add items to favorite
def add_favorite(request):
    product_id = request.GET.get('product')
    product=Product.objects.get(id=product_id)
    data={}
    try:
        #if product already exist in favorite deleting it 
        favorite_list=FavoriteItem.objects.get(product=product,user=request.user)
        favorite_list.delete()
        data={
            'state':False
        }
    except FavoriteItem.DoesNotExist:
        favorite_list=FavoriteItem.objects.create(product=product,user=request.user)
        data={
            'state':True
        }

    return JsonResponse(data)



def favorites_list(request):
    product=FavoriteItem.objects.filter(user=request.user)
    context={
        'product':product
    }
    return render(request,'favourites.html',context)


@login_required(login_url='User:login')
def chat(request):
    return render(request,'chat.html')