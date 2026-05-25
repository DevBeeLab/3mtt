from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from product.models import Product, ProductTransactions
from django.contrib import messages
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Products (LoginRequiredMixin, View):
    def get(self, request):
        all_products = Product.objects.all().order_by('-created_at')        
        return render(request, 'product.html', {'all_prod': all_products})


class AddProduct(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'add_product.html')
    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        image = request.FILES.get('image')

        if not name or not description or not price or not quantity or not image:
            messages.error(request, 'all field are required')
            return redirect(resolve_url('add-product'))

        quantity = int(quantity)
        price = int(price)

        try:
            quantity = int(quantity)
            price = int(price)
        except ValueError:
            messages.error(request, 'price and quantity must be numbers')
            return redirect(resolve_url('add-product'))

        if price < 1:
            messages.error(request, 'price must be greater than 0')
            return redirect(resolve_url('add-product'))
        if quantity < 1:
            messages.error(request, 'quantity must be greater than 0')
            return redirect(resolve_url('add-product'))
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            image=image,
            user=request.user
        )   

        # return render(request, 'product.html', {'message': 'Product added successfully!'})
        return redirect(resolve_url('products'))

class EditProduct(LoginRequiredMixin, View):
    def get(self, request, product_id):
        product = Product.objects.filter(id=product_id).first()
        if not product:
            messages.error(request, 'product not found')
            return redirect(resolve_url('products'))
        if product.user != request.user:
            messages.error(request, 'you are not allowed to edit this product')
            return redirect(resolve_url('products'))
        return render(request, 'edit_product.html', {'product': product})
    def post(self, request, product_id):
        product = Product.objects.filter(id=product_id).first()
        if not product:
            messages.error(request, 'product not found')
            return redirect(resolve_url('products'))
        if product.user != request.user:
            messages.error(request, 'you are not allowed to edit this product')
            return redirect(resolve_url('products'))

        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        image = request.FILES.get('image')
 
        product.name = name or product.name
        product.description = description or product.description
        product.price = price or product.price
        product.quantity = quantity or product.quantity
        product.image = image or product.image
        product.save()
        messages.success(request, 'product successfully updated')
        return redirect(resolve_url('products'))

@login_required
def delete_product(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if not product:
        messages.error(request, 'product not found')
        return redirect(resolve_url('products'))
    if product.user != request.user:
        messages.error(request, 'you are not allowed to edit this product')
        return redirect(resolve_url('products'))
    product.delete()
    messages.error(request, 'product successfully deleted')
    return redirect(resolve_url('products'))
    

@login_required
def buy_product(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if not product:
        messages.error(request, 'product not found')
        return redirect(resolve_url('products'))
    if product.user == request.user:
        messages.error(request, 'you are not allowed to buy your product')
        return redirect(resolve_url('products'))
    if request.method == 'GET':
        return render(request, 'buy_product.html', {'product': product})

    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('quantity'))
        except (TypeError, ValueError):
            messages.error(request, 'enter a valid quantity')
            return redirect(resolve_url('buy-product', product.id))
        if quantity <= 0:
            messages.error(request, 'quantity must be greater than zero')
            return redirect(resolve_url('buy-product', product.id))
        if quantity > product.quantity:
            messages.error(request, 'not enough stock available')
            return redirect(resolve_url('buy-product', product.id))
        product.quantity -= quantity
        product.sold += quantity
        ProductTransactions.objects.create(
            product=product,
            user=request.user,
            price=product.price,
            quantity=quantity,
            quantity_left=product.quantity,
            sold=product.sold
        )     
        product.save()
        messages.success(request, 'product bought successfully')
        return redirect(resolve_url('products'))
    
def error_404_view(request, exception):
    return render(request, 'error_404.html')

def error_500_view(request):
    return render(request, 'error_500.html')