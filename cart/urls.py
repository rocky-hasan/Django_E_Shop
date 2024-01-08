from django.urls import path
from . import views


urlpatterns = [
   path('',views.CartView.as_view(), name='cart_summary'),
   path('add/',views.Cart_addView.as_view(), name='cart_add'),
   path('delete/',views.Cart_deleteView.as_view(), name='cart_delete'),
   path('update/',views.Cart_updateView.as_view(), name='cart_update'),
]