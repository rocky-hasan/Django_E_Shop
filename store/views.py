from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from .models import Product,Category
from django.contrib import messages

# Create your views here.
class Home(View):
    def get(self,request):
        products=Product.objects.all()
        return render(request, 'home.html',{'products':products})
class About(View):
    def get(self,request):     
        return render(request, 'about.html',{})
class Product_detail(View):
    def get(self,request,pk):     
        products=Product.objects.get(id=pk)
        return render(request, 'product.html',{'product':products})

class CategoryView(View):
    def get(self, request, foo):
        foo = foo.replace('-', ' ')
        try:
            category = Category.objects.get(name=foo)
            products = Product.objects.filter(category=category)
            return render(request, 'category.html', {'products': products, 'category': category})
        except Category.DoesNotExist:
            messages.success(request, "That Category Doesn't Exist...")
            return redirect('home')