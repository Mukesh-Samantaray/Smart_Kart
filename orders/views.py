from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.models import CartItem
from profiles.models import Address
from django.http import JsonResponse

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_list_api(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    data = []
    for order in orders:
        data.append({
            'id': order.id,
            'total_price': order.total_price,
            'status': order.status,
            'payment_method': order.payment_method,
            'is_paid': order.is_paid,
            'created_at': order.created_at.isoformat(),
        })
    return JsonResponse({'orders': data})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def order_detail_api(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    items = order.orderitem_set.all()
    items_data = []
    for item in items:
        items_data.append({
            'product_name': item.product.name,
            'quantity': item.quantity,
            'price': item.price,
        })
    data = {
        'id': order.id,
        'total_price': order.total_price,
        'status': order.status,
        'payment_method': order.payment_method,
        'is_paid': order.is_paid,
        'created_at': order.created_at.isoformat(),
        'items': items_data,
    }
    return JsonResponse({'order': data})

@login_required
def create_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        return redirect('cart:cart_detail')

    addresses = Address.objects.filter(user=request.user)

    if request.method == 'POST':
        address_id = request.POST.get('address_id')
        address = addresses.get(id=address_id) if address_id else None
        payment_method = request.POST.get('payment_method')  # 👈 capture COD or Online

        order = Order.objects.create(
            user=request.user,
            address=address,
            total_price=sum(item.product.price * item.quantity for item in cart_items),
            status="Yet to be Delivered" if payment_method == "cod" else "Pending",
            payment_method=payment_method
        
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # Clear cart after order
        cart_items.delete()

        if payment_method == "cod":
            print("DEBUG payment_method:", payment_method)
            # COD → Show success message & redirect to profile/orders
            from django.contrib import messages
            messages.success(request, "Order placed successfully! Happy shopping 🎉")
            return render(request, "orders/order_success.html", {"order": order})

        else:
            # Online payment → Redirect to payment page
            return redirect('orders:payment', pk=order.pk)

    # GET request: show address + payment option
    return render(request, 'orders:select_address.html', {'cart_items': cart_items, 'addresses': addresses})

@login_required
def cancel_order(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    if order.status == "Pending":   # only allow cancel if not processed
        order.status = "Cancelled"
        order.save()
    return redirect('orders:order_detail', pk=pk)
import random
import time

@login_required
def payment(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    print("DEBUG payment_method:", order.payment_method)
    print("DEBUG is_paid:", order.is_paid)
    upi_id = "your-upi-id@okbank"
    amount = order.total_price
    upi_url = f"upi://pay?pa={upi_id}&pn=SmartKart&am={amount}&cu=INR"

    if request.method == "POST" and order.payment_method == "online" and not order.is_paid:
        time.sleep(5)  # Wait for 5 seconds to simulate payment processing
        result = random.choice(["success", "fail"])
        if result == "success":
            order.is_paid = True
            order.save()
            return render(request, "orders/payment_success.html", {"order": order})
        else:
            return render(request, "orders/payment_failed.html", {"order": order})
    return render(request, 'orders/payment.html', {
        'order': order,
        'upi_url': upi_url,
        'upi_id': upi_id,
        'amount': amount
    })
def track_order(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'orders/track_order.html', {'order': order})

@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "orders/order_success.html", {"order": order})
