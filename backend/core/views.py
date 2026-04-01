import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import ShopProduct, Order, ShopCategory


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['shopproduct_count'] = ShopProduct.objects.count()
    ctx['shopproduct_active'] = ShopProduct.objects.filter(status='active').count()
    ctx['shopproduct_draft'] = ShopProduct.objects.filter(status='draft').count()
    ctx['shopproduct_out_of_stock'] = ShopProduct.objects.filter(status='out_of_stock').count()
    ctx['shopproduct_total_price'] = ShopProduct.objects.aggregate(t=Sum('price'))['t'] or 0
    ctx['order_count'] = Order.objects.count()
    ctx['order_pending'] = Order.objects.filter(status='pending').count()
    ctx['order_processing'] = Order.objects.filter(status='processing').count()
    ctx['order_shipped'] = Order.objects.filter(status='shipped').count()
    ctx['order_total_total'] = Order.objects.aggregate(t=Sum('total'))['t'] or 0
    ctx['shopcategory_count'] = ShopCategory.objects.count()
    ctx['shopcategory_active'] = ShopCategory.objects.filter(status='active').count()
    ctx['shopcategory_hidden'] = ShopCategory.objects.filter(status='hidden').count()
    ctx['recent'] = ShopProduct.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def shopproduct_list(request):
    qs = ShopProduct.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'shopproduct_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def shopproduct_create(request):
    if request.method == 'POST':
        obj = ShopProduct()
        obj.name = request.POST.get('name', '')
        obj.sku = request.POST.get('sku', '')
        obj.category = request.POST.get('category', '')
        obj.price = request.POST.get('price') or 0
        obj.compare_price = request.POST.get('compare_price') or 0
        obj.stock = request.POST.get('stock') or 0
        obj.status = request.POST.get('status', '')
        obj.weight = request.POST.get('weight') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/shopproducts/')
    return render(request, 'shopproduct_form.html', {'editing': False})


@login_required
def shopproduct_edit(request, pk):
    obj = get_object_or_404(ShopProduct, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.sku = request.POST.get('sku', '')
        obj.category = request.POST.get('category', '')
        obj.price = request.POST.get('price') or 0
        obj.compare_price = request.POST.get('compare_price') or 0
        obj.stock = request.POST.get('stock') or 0
        obj.status = request.POST.get('status', '')
        obj.weight = request.POST.get('weight') or 0
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/shopproducts/')
    return render(request, 'shopproduct_form.html', {'record': obj, 'editing': True})


@login_required
def shopproduct_delete(request, pk):
    obj = get_object_or_404(ShopProduct, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/shopproducts/')


@login_required
def order_list(request):
    qs = Order.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(order_number__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'order_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def order_create(request):
    if request.method == 'POST':
        obj = Order()
        obj.order_number = request.POST.get('order_number', '')
        obj.customer_name = request.POST.get('customer_name', '')
        obj.customer_email = request.POST.get('customer_email', '')
        obj.total = request.POST.get('total') or 0
        obj.status = request.POST.get('status', '')
        obj.payment_status = request.POST.get('payment_status', '')
        obj.order_date = request.POST.get('order_date') or None
        obj.shipping_address = request.POST.get('shipping_address', '')
        obj.save()
        return redirect('/orders/')
    return render(request, 'order_form.html', {'editing': False})


@login_required
def order_edit(request, pk):
    obj = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        obj.order_number = request.POST.get('order_number', '')
        obj.customer_name = request.POST.get('customer_name', '')
        obj.customer_email = request.POST.get('customer_email', '')
        obj.total = request.POST.get('total') or 0
        obj.status = request.POST.get('status', '')
        obj.payment_status = request.POST.get('payment_status', '')
        obj.order_date = request.POST.get('order_date') or None
        obj.shipping_address = request.POST.get('shipping_address', '')
        obj.save()
        return redirect('/orders/')
    return render(request, 'order_form.html', {'record': obj, 'editing': True})


@login_required
def order_delete(request, pk):
    obj = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/orders/')


@login_required
def shopcategory_list(request):
    qs = ShopCategory.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'shopcategory_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def shopcategory_create(request):
    if request.method == 'POST':
        obj = ShopCategory()
        obj.name = request.POST.get('name', '')
        obj.parent = request.POST.get('parent', '')
        obj.products_count = request.POST.get('products_count') or 0
        obj.position = request.POST.get('position') or 0
        obj.status = request.POST.get('status', '')
        obj.image_url = request.POST.get('image_url', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/shopcategories/')
    return render(request, 'shopcategory_form.html', {'editing': False})


@login_required
def shopcategory_edit(request, pk):
    obj = get_object_or_404(ShopCategory, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.parent = request.POST.get('parent', '')
        obj.products_count = request.POST.get('products_count') or 0
        obj.position = request.POST.get('position') or 0
        obj.status = request.POST.get('status', '')
        obj.image_url = request.POST.get('image_url', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/shopcategories/')
    return render(request, 'shopcategory_form.html', {'record': obj, 'editing': True})


@login_required
def shopcategory_delete(request, pk):
    obj = get_object_or_404(ShopCategory, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/shopcategories/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['shopproduct_count'] = ShopProduct.objects.count()
    data['order_count'] = Order.objects.count()
    data['shopcategory_count'] = ShopCategory.objects.count()
    return JsonResponse(data)
