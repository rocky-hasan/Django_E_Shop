from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView,View
from django.contrib import messages
from store.models import Product,Category
from django.http import JsonResponse
from .cart import CartView

# Create your views here.
class CartView(View):
    def get(self, request):
        cart = CartView(request)
        cart_products = cart.get_prouduct()
        return render(request, 'Cart/cart.html', {'cart_products': cart_products})
    
class Cart_addView(View):
    def get(self,request):
        cart=CartView(request)
        return render(request, 'Cart/cart.html',{})
    def post(self,request):
        #collect the cart
        cart=CartView(request)
        if request.POST.get('action')=='POST':
            product_id=int(request.POST.get('product_id'))
            # get product 
            product=get_object_or_404(Product,id=product_id)
            # save it session
            cart.add(product=product)
            response= JsonResponse ({'Product Name': product.name})
            return response
    
class Cart_deleteView(View):
    def get(self,request):
        return render(request, 'Cart/cart.html',{})
    
class Cart_updateView(View):
    def get(self,request):
        return render(request, 'Cart/cart.html',{})