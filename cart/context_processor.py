
def cart_total_count(request):
    from .models import CartItem
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_qty = sum(item.quantity for item in cart_items)
        total_price = sum(item.total_price() for item in cart_items)
    else:
        total_qty = 0
        total_price = 0

    return {
        'cart_total_qty': total_qty,
        'cart_total_price': total_price
    }
