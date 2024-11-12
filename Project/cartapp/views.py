from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Cart, CartItems
from django.shortcuts import get_object_or_404
from .models import Cart, CartItems, ProductDetails
from django.urls import reverse
from django.http import HttpResponse
import stripe
from django.http import HttpResponse
from django.conf import settings

# cart
def view_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        cart_items = CartItems.objects.filter(cart=cart)
        
        total_price = sum(item.book.price * item.quantity for item in cart_items)
        total_items = cart_items.count()
        total1 = 0
        
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        cart_i = cart.cartitems_set.all()
        total_product = cart_i.count()
        
        discount = 0
        for item in cart_items:
            item.calculated = item.book.price * item.quantity
            total1 += item.calculated
            if item.quantity != 0: 
                discount += 100 * item.quantity
            else:
                discount += 100
        print(discount)
        total2 = total1 - discount 
        
      
        context = {
            'cart_items': cart_items,
            'total_product': total_product,
            'cart_items': cart_items, 
            'total_price': total_price, 
            'total_items': total_items,
            'total1':total1,
            'discount':discount,
            'total':total2,
            
        }
       
    else:
       
        messages.error(request,"Login Required")
        return redirect("login")

    return render(request, 'cart.html', context)

#Add items to the cart
def add_to_cart(request,id):
   
    product = get_object_or_404(ProductDetails, id=id)
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItems.objects.get_or_create(cart=cart, book=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    else:
        cart = request.session.get('cart', {})
        cart[str(id)] = cart.get(str(id), 0) + 1
        request.session['cart'] = cart

    return redirect('viewcart')  

#Increase quantity
def increase_quantity(request,id):
    cart_item=CartItems.objects.get(id=id)

    if cart_item.quantity < cart_item.book.quantity :
        cart_item.quantity +=1
        cart_item.save() 

    return redirect('viewcart')

#Decrease quantity
def decrease_quantity(request,id):
    cart_item=CartItems.objects.get(id=id)

    if cart_item.quantity > 1 :
        cart_item.quantity -=1
        cart_item.save() 

    return redirect('viewcart')

#Remove item from the cart
def remove_cart(request,id):
    try:
        cart_item=CartItems.objects.get(id=id)
        cart_item.delete()
    except cart_item.DoesNotExist:
        pass

    return redirect('viewcart')
 

stripe.api_key = settings.STRIPE_SECRET_KEY

# Payment Section
def Payment(request):
    cart_items = CartItems.objects.all()  

    if not cart_items.exists():
        return HttpResponse("Your cart is empty", status=400)
    
    if request.method == 'POST':
        line_items = []
        for cart_item in cart_items:
            if cart_item.book:
                line_item = {
                    'price_data': {
                        'currency': 'INR',
                        'unit_amount': int(  cart_item.book.price  * 100 )-10000,  
                        'product_data': {
                            'name': cart_item.book.name,
                        },
                },
                    'quantity': cart_item.quantity,
                }
                line_items.append(line_item)
        if not line_items:
            return HttpResponse("No valid items in cart to process", status=400)

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=request.build_absolute_uri(reverse('success')),
                cancel_url=request.build_absolute_uri(reverse('cancel')),
            )
            return redirect(checkout_session.url, code=303)
        except stripe.error.StripeError as e:
            print(f"Stripe Error: {e}")
            return HttpResponse("Error in creating checkout session", status=500)

    return HttpResponse("Invalid request method", status=405)

# After successful transaction
def Success(request):
    cart_items=CartItems.objects.all()

    for cart_item in cart_items:
        product=cart_item.book
        if product.quantity >= cart_item.quantity :
            product.quantity -=cart_item.quantity
            product.save()

    cart_items.delete()
    return render(request,'success.html')

def Cancel(request):
    return render(request,'cancel.html')



