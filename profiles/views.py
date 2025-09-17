from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Address
from .forms import AddressForm

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    addresses = request.user.addresses.all()
    orders = request.user.orders.all().order_by('-created_at')  # add orders here
    return render(request, "profiles/profile_detail.html", {
        "profile": profile,
        "addresses": addresses,
        "orders": orders,
    })

@login_required
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user  # ✅ attach the actual User instance
            address.save()
            return redirect('profiles:profile')
    else:
        form = AddressForm()
    return render(request, 'profiles/address_form.html', {'form': form})

@login_required
def edit_address(request, pk):
    # ✅ filter by user, not profile
    address = get_object_or_404(Address, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('profiles:profile')
    else:
        form = AddressForm(instance=address)
    return render(request, 'profiles/address_form.html', {'form': form})

@login_required
def delete_address(request, pk):
    # ✅ filter by user, not profile
    address = get_object_or_404(Address, pk=pk, user=request.user)
    if request.method == 'POST':
        address.delete()
        return redirect('profiles:profile')
    return render(request, 'profiles/address_confirm_delete.html', {'address': address})
