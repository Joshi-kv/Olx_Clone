from django.shortcuts import render

# Create your views here.

def chat_page(request):
    product_image = request.GET.get('product_image')
    owner_name = request.GET.get('owner_name')
    context={
        'product_image':product_image,
        'owner_name':owner_name
    }
    return render(request, 'chat.html',context )
