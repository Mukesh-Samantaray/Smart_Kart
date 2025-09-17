from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from products.models import Product
from .models import CartItem
from profiles.models import Address

@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_total = sum(item.total_price() for item in cart_items)
    addresses = Address.objects.filter(user=request.user)
    return render(request, "cart/cart_detail.html", {"cart_items": cart_items, "cart_total": cart_total, "addresses": addresses})


@login_required
def add_to_cart(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1
        cart_item.save()
    return redirect("cart:cart_detail")

@csrf_exempt
@login_required
def add_to_cart_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)
        user = request.user

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found'}, status=404)

        cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        return JsonResponse({'message': f'Added {quantity} of {product.name} to cart.'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)



@login_required
def remove_from_cart(request, product_id):
    if request.method == "POST":
        cart_item = get_object_or_404(CartItem, user=request.user, product_id=product_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()  # remove completely if quantity is 1
    return redirect("cart:cart_detail")
