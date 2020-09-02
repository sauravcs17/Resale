from django.shortcuts import render, redirect
from .models import Product, ProductImages, Category, Seller
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .forms import ProductForm, ImageForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
import sqlite3
from django.http import HttpResponseRedirect
from django.utils import timezone


# Create your views here.
def productlist(request, category_slug=None):
    category = None
    # this_month = timezone.now().month
    # productl = Product.objects.all()
    product = Product.objects.all().order_by('-created')
    # productlist = Product.objects.all()
    categorylist = Category.objects.annotate(total_products=Count('product'))
    # print(product_list)
    if category_slug:
        # category=Category.objects.get(slug=category_slug)
        category = get_object_or_404(Category, slug=category_slug)
        product = product.filter(category=category)

    search_query = request.GET.get('q')
    if search_query:
        product = product.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(condition__icontains=search_query) |
            Q(brand__brand_name__icontains=search_query)
        )

    paginator = Paginator(product, 4)  # Show 25 contacts per page

    page = request.GET.get('page')
    product = paginator.get_page(page)

    context = {'product_list': product, 'category_list': categorylist, 'category': category}

    template = 'product_list.html'

    return render(request, template, context)

'''
def productdetails(request, product_slug):
    # print(product_slug)
    # productdetail = Product.objects.get(slug=product_slug)

    productdetail = get_object_or_404(Product, slug=product_slug)
    data = Seller.objects.get(user__id=request.user.id)

    productimage = ProductImages.objects.filter(product=productdetail)

    if request.user.is_authenticated:
        if request.method == 'POST':
            image_form = ImageForm(data=request.POST, files=request.FILES)
            if image_form.is_valid():
                instance = image_form.save(commit=False)

                instance.product = productdetail
                instance.save()
                return redirect('/')
        else:
            image_form = ImageForm()

    context = {'product_detail': productdetail, 'product_images': productimage, 'image_form': image_form, 'data': data}

    template = 'product_details.html'

    return render(request, template, context)
'''

def delete(request, product_slug):
    obj = get_object_or_404(Product, slug=product_slug)
    if request.method == "POST":
        obj.delete()
        return redirect('/')
    context = {
        'object': obj
    }

    return render(request, "delete.html", context)


def postadd(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post_form = ProductForm(data=request.POST, files=request.FILES)
            if post_form.is_valid():
                instance = post_form.save(commit=False)
                instance.owner = request.user
                instance.save()
                return redirect('/')
        else:
            post_form = ProductForm()

    context = {'post_form': post_form}
    template = 'post-ad.html'

    return render(request, template, context)



def productdetails(request, product_slug):
    # print(product_slug)
    # productdetail = Product.objects.get(slug=product_slug)

    productdetail = get_object_or_404(Product, slug=product_slug)
    data = Seller.objects.get(user__id=request.user.id)

    productimage = ProductImages.objects.filter(product=productdetail)

    if request.user.is_authenticated:
        if request.method == 'POST':
            image_form = ImageForm(data=request.POST, files=request.FILES)
            if len(request.FILES) != 0:
                if image_form.is_valid():
                    instance = image_form.save(commit=False)
                    instance.product = productdetail
                    instance.save()
                    messages.info(request,"Video Added !!!")
            else:
                messages.info(request,"No File Choosen !!!")

        else:
            image_form = ImageForm()

    context = {'product_detail': productdetail, 'product_images': productimage, 'image_form': image_form, 'data': data}

    template = 'product_details.html'

    return render(request, template, context)


