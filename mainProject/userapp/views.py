from django.shortcuts import render
from myapp.models import ProductDetails
from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from cartapp.models import Cart
from django.contrib.auth import authenticate, login

# Slider in home page
def UserTest(request):
    products = ProductDetails.objects.all()
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        cart_items = cart.cartitems_set.all()
        total_product = cart_items.count()
        context = {
            'cart_items': cart_items,
            'total_product': total_product,
            'products':products
        }
        print(total_product)
        return render(request,'slider.html',context)
    else:
        return render(request,'slider.html',{'products':products})
    
# Store
def Store(request):
    products = ProductDetails.objects.all()
    paginator=Paginator(products,12)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)
        
    products = ProductDetails.objects.all()
    
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        cart_items = cart.cartitems_set.all()
        total_product = cart_items.count()
        context = {
            'cart_items': cart_items,
            'total_product': total_product,
            'products':products,
            'products':products,
            'page':page
        }
        print(total_product)
        return render(request,'store.html',context)
    else:
        return render(request,'store.html',{'products':products,'page':page})
   
    

def test(request):
    products = ProductDetails.objects.all()
    return render(request,'testing.html',{'products':products})

# Checkout
def Checkout(request,id):
    product = ProductDetails.objects.get(id=id)
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        cart_i = cart.cartitems_set.all()
        total_product = cart_i.count()
        context = {
            'cart_items': cart_i,
            'total_product': total_product,
            'product':product,
        }
        print(total_product)
        return render(request,'checkout.html',context)
    else:
        return render(request,'checkout.html',{'product':product})
    
# Search
def Search(request):
    query=None
    content=None
    if 'qe' in request.GET:
        query=request.GET.get('qe')
        content=ProductDetails.objects.filter(Q(name__icontains=query))
    else:
        content=[]
    return render(request,'search.html',{'query':query,'content':content})

# Register function
def Register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if not email:
            messages.error(request, "Email field cannot be empty.")
            return redirect('register')
        if not password:
            messages.error(request, "Password field cannot be empty.")
            return redirect('register')
        if not confirm_password:
            messages.error(request, "Confirm password field cannot be empty.")
            return redirect('register')
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('register')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        messages.success(request, "Register success.")
        return redirect('login')

    return render(request, 'Registerpage.html')

# Login functn
def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_staff or user.is_superuser:  
                return redirect(reverse('dash'))  
            else:
                return redirect(reverse('home'))  
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')

    return render(request, 'Loginpage.html')



def Logout(request):
    logout(request)  
    return redirect('home') 

 

