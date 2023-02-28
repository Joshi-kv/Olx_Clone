from django.urls import path
from . import views
app_name='Home'
urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('<slug:category_slug>/',views.home_page,name='products_by_category'),
    path('addproduct',views.sell_product,name='addproduct'),
    path('<slug:category_slug>/<int:product_id>/',views.product_details,name='product_details'),
    path('search?=/',views.search,name='search'),
]
