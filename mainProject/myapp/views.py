from django.shortcuts import render, redirect
from .models import ProductDetails
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def staff_or_admin_check(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

# Create product
def CreateProduct(request):
    if not (request.user.is_staff or request.user.is_superuser):
        return render(request,'notfound.html')  
    if request.method == "POST":
        name=request.POST.get('name')
        quantity=request.POST.get('quantity')
        price=request.POST.get('price')
        image=request.FILES.get('image')

        if name and quantity and price and image:
            product = ProductDetails(name=name, quantity=quantity, price = price, image=image)
            product.save()
            messages.error(request, "Insertion successful!")
            return redirect("dash")
        else:
            messages.error(request, "Insertion Failed!")
    return render(request,"createProduct.html")

# @user_passes_test(staff_or_admin_check, redirect_field_name='notfound')
def Pro_Details(request):
    if not (request.user.is_staff or request.user.is_superuser):
        return render(request,'notfound.html')  
    products=ProductDetails.objects.all()
    return render(request,"index.html",{'products':products})

# Product update
def Pro_Update(request, id):
    if not (request.user.is_staff or request.user.is_superuser):
        return render(request,'notfound.html')  
    product=ProductDetails.objects.get(id=id)
    if request.method == "POST":
        name=request.POST.get('name')
        quantity=request.POST.get('quantity')
        price=request.POST.get('price')
        image=request.FILES.get('image')

        if name and quantity and price:
                if image:
                    product.image = image  
                product.name = name  
                product.quantity = quantity  
                product.price = price
                product.save()
                messages.error(request, "Updation successful!")
                return redirect("dash")
        else:
            messages.error(request, "Updation Failed!")
    return render(request,"update.html",{"product":product})

# Delete product
def Pro_Delete(request, id):
    if not (request.user.is_staff or request.user.is_superuser):
        return render(request,'notfound.html')  
    product = get_object_or_404(ProductDetails, id=id)  
    if request.method == 'POST':
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect('dash')
    return render(request, 'index.html', {'product': product})

#Search product
def Pro_Search(request):
    if not (request.user.is_staff or request.user.is_superuser):
        return render(request,'notfound.html')  
    query=None
    content=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        content=ProductDetails.objects.filter(Q(name__icontains=query) | Q(price__exact=query))
    else:
        content=[]
    return render(request,'adminSearch.html',{'query':query,'content':content})





def test(request):
    if not (request.user.is_staff or request.user.is_superuser):
        return render(request,'notfound.html')  
    query=None
    content=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        print(query)
        content=ProductDetails.objects.filter(Q(name__icontains=query) | Q(price__icontains=query))
    else:
        content=[]
        print("Element not found..")
    return render(request,'test.html',{'query':query,'content':content})


def notfound(request):
    return(render,'notfound.html')



