from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from products.models import Category, Product


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    # Show all products after login
    if not request.user.is_authenticated:
        from django.shortcuts import redirect
        return redirect('login')

    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, "accounts/home.html", {
        "categories": categories,
        "products": products
    })
