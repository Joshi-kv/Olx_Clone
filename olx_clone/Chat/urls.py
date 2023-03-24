from django.urls import path
from . import views

app_name="Chat"

urlpatterns = [
    path('chat/',views.chat,name='chat'),
    path('new-chat/<int:product_id>/',views.chat_page,name='chat_page'),
]
