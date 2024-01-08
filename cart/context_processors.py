from .cart import CartView
# create context prcessor that cart can do work all pages
def cart(request):

    return {'cart':CartView(request)} #its return default data if it has or not