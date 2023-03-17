from django.urls import path
from . import views
app_name='Home'
urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('add_favorite/',views.add_favorite,name='add_favorite'),
    path('favorites_list/',views.favorites_list,name='favorites_list'),
    path('my_adds/',views.my_adds,name='myadds'),
    path('remove_adds/',views.remove_adds,name="remove_adds"),
    path('<slug:category_slug>/',views.home_page,name='products_by_category'),    
    path('<slug:category_slug>/',views.my_adds,name='myadds'),
    path('addproduct',views.sell_product,name='addproduct'),
    path('<slug:category_slug>/<int:product_id>/',views.product_details,name='product_details'),
    path('search?=/',views.search,name='search'),
    
    
]
