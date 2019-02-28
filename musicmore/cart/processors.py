from .models import Cart, CartItem
from .views import _cart_id

def ctx_dict_cart(request):
    cart = Cart.objects.filter(cart_id=_cart_id(request))
    cart_items = CartItem.objects.all().filter(cart=cart[:1])    
    ctx_cart = {'CTX_CART_ITEMS':cart_items}
    return ctx_cart

