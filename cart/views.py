from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView,View
from django.contrib import messages
from store.models import Product,Category
from django.http import JsonResponse
from .cart import CartView

# Create your views here.

def cart_summary(request):
	# Get the cart
	cart = CartView(request)
	cart_products = cart.get_prouduct
	quantities = cart.get_quants
	totals = cart.cart_total()              
	return render(request, "Cart/cart.html", {"cart_products":cart_products, "quantities":quantities  , "totals":totals})

    
def cart_add(request):
    # Get the cart
    cart = CartView(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        
        # Save to session
        cart.add(product=product, quantity=product_qty)

        # Get Cart Quantity
        cart_quantity = cart.__len__()

        # Return resonse
        response = JsonResponse({'qty': cart_quantity})
        messages.success(request, "Product Added To Cart...")
        return response

    
    
def cart_delete(request):
    cart = CartView(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.get_delete(product=product_id)
        response=JsonResponse({'product':product_id})
        return response
    
def cart_update(request):
    # Get the cart
    cart = CartView(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id,quantity=product_qty)
        response=JsonResponse({'qty':product_qty})
        return response
    return redirect('cart_summary')