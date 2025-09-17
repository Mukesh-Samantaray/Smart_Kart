from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q

# Show all products
def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "products/product_list.html", {"products": products, "categories": categories})


# Product detail
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related = Product.objects.filter(category=product.category).exclude(id=pk)[:4]
    return render(request, "products/product_detail.html", {"product": product, "related": related})


# Filter by category
def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, "products/product_list.html", {"products": products, "categories": categories, "selected_category": category})


# Search products
def search_products(request):
    query = request.GET.get("q")
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)) if query else []
    categories = Category.objects.all()
    return render(request, "products/product_list.html", {"products": products, "categories": categories, "search_query": query})
