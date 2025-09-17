from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
import google.generativeai as genai
from django.conf import settings
from orders.models import Order
from products.models import Product
from cart.models import CartItem

# Configure Gemini
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


@login_required
@csrf_exempt
def chatbot_view(request):
    if request.method != "POST":
        return JsonResponse({"response": "Invalid request method."})

    data = json.loads(request.body)
    user_message = data.get("message", "")
    user_name = request.user.first_name or request.user.username

    # Step 1: Ask Gemini for decision
    decision_prompt = f"""
    You are SmartKart assistant for user {user_name}.
    User query: "{user_message}"

    Decide if the answer should come from SmartKart data:
    - "orders" → when user asks about their orders or history
    - "products" → when user asks about products, categories, specs, prices, suggestions
    - "tracking" → when user asks about delivery status or shipment
    - "cart" → when user asks about cart items
    - "general" → for everything else

    Respond with exactly one word only: orders, products, tracking, cart, general
    """
    try:
        gemini_decision = model.generate_content(decision_prompt)
        decision_text = (
            gemini_decision.text.strip().lower()
            if gemini_decision and hasattr(gemini_decision, "text")
            else "general"
        )
    except Exception:
        decision_text = "general"

    bot_reply = f"Hello {user_name}, I'm not sure how to answer that right now."

    # Step 2: Handle each case
    try:
        if decision_text == "orders":
            orders = Order.objects.filter(user=request.user).order_by("-created_at")[:5]
            if orders.exists():
                order_list = [f"Order {o.id}: {o.status} - ₹{o.total_price}" for o in orders]
                bot_reply = "Here are your recent orders:\n" + "\n".join(order_list)
            else:
                bot_reply = "You have no orders yet."

        elif decision_text == "products":
            products = Product.objects.all().order_by("price")[:5]
            if products.exists():
                product_list = [f"{p.name} - ₹{p.price}" for p in products]
                bot_reply = "Available products:\n" + "\n".join(product_list)
            else:
                bot_reply = "No products available right now."

        elif decision_text == "tracking":
            orders = (
                Order.objects.filter(user=request.user)
                .exclude(status="Delivered")
                .order_by("-created_at")[:3]
            )
            if orders.exists():
                track_list = [f"Order {o.id}: {o.status}" for o in orders]
                bot_reply = "Your active orders:\n" + "\n".join(track_list)
            else:
                bot_reply = "No active orders to track."

        elif decision_text == "cart":
            cart_items = CartItem.objects.filter(user=request.user)
            if cart_items.exists():
                cart_list = [f"{item.product.name} ×{item.quantity}" for item in cart_items]
                bot_reply = "Your cart:\n" + "\n".join(cart_list)
            else:
                bot_reply = "Your cart is empty."

        else:  # general
            gen_response = model.generate_content(
                f"You are SmartKart AI assistant. User {user_name} asked: {user_message}. Respond conversationally."
            )
            bot_reply = gen_response.text

    except Exception as e:
        bot_reply = f"Sorry {user_name}, error fetching info: {str(e)}"

    return JsonResponse({"response": bot_reply})
