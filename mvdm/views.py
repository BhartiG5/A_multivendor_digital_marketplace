from django.shortcuts import render, redirect
from .models import Product,OrderDetail
from .forms import  ProductForm, UserRegistrationForm, LoginForm
from django.db.models import Sum
import datetime
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    products = Product.objects.all()

    # paginator code
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(request,'mvdm/index.html',{'products':products})

def detail(request,id):
    product=Product.objects.get(id=id)
    return render(request, 'mvdm/detail.html',{'product':product})

def create_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST,request.FILES)
        if product_form.is_valid():
            new_product = product_form.save(commit=False)
            new_product.seller = request.user
            new_product.save()
            return redirect('mvdm:index')
    else:
        product_form = ProductForm()
    return render(request,'mvdm/create_product.html',{'product_form':product_form})

def product_edit(request,id):
    product = Product.objects.get(id=id)
    if product.seller != request.user:
        return redirect('mvdm:invalid')
    product_form = ProductForm(request.POST or None,request.FILES or None, instance=product)
    if request.method == 'POST':
        if product_form.is_valid():
            product_form.save()
            return redirect('mvdm:index')
    return render(request, 'mvdm/product_edit.html',{'product_form':product_form,'product':product})

def product_delete(request,id):
    product = Product.objects.get(id=id)
    if product.seller != request.user:
        return redirect('mvdm:invalid')
    if request.method == 'POST':
        product.delete()
        return redirect('mvdm:index')
    return render(request, 'mvdm/delete.html',{'product':product})

def dashboard(request):
    products = Product.objects.filter(seller=request.user)
    return render(request,'mvdm/dashboard.html', {'products':products})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created')
            return redirect('mvdm:login')
    else:
        user_form = UserRegistrationForm()
    return render(request,'mvdm/register.html',{'user_form':user_form})

def login_view(request):
    if request.method == 'POST':
        form=LoginForm(request.POST) 
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['username'], password=data['password'])
            if user is not None:
                login(request,user)
                return redirect('mvdm:index')
            else:
                return HttpResponse("Invalid credentials")
    else:
        form = LoginForm()
        return render(request,'mvdm/login.html',{'form':form})


def invalid(request):
    return render(request, 'mvdm/invalid.html')

def my_purchases(request):
    orders = OrderDetail.objects.filter(customer_email= request.user.email)

    return render(request, 'mvdm/purchases.html',{'orders':orders})


def sales(request):
    orders = OrderDetail.objects.filter(product__seller=request.user)
    total_sales = orders.aggregate(Sum('amount'))
    print(total_sales)

    # 365 days sales sum
    last_year = datetime.date.today()- datetime.timedelta(days=365)
    data = OrderDetail.objects.filter(product__seller=request.user, created_on__gt = last_year)
    yearly_sales = data.aggregate(Sum('amount'))

    # 30 days sales sum
    last_month = datetime.date.today()- datetime.timedelta(days=30)
    data = OrderDetail.objects.filter(product__seller=request.user, created_on__gt = last_month)
    monthly_sales = data.aggregate(Sum('amount'))

    # 7 days sales sum
    last_weak = datetime.date.today()- datetime.timedelta(days=2)
    data = OrderDetail.objects.filter(product__seller=request.user, created_on__gt = last_weak)
    weakly_sales = data.aggregate(Sum('amount'))

    # everyday sum for the past 30 days
    daily_sales_sums = OrderDetail.objects.filter(product__seller= request.user).values('created_on__date').order_by('created_on__date').annotate(sum=Sum('amount'))
    print(daily_sales_sums)

    product_sales_sums = OrderDetail.objects.filter(product__seller= request.user).values('product__name').order_by('product__name').annotate(sum=Sum('amount'))
    print(product_sales_sums)


    return render(request ,'mvdm/sales.html',{'total_sales':total_sales,'yearly_sales':yearly_sales,'monthly_sales':monthly_sales,'weakly_sales':weakly_sales,'daily_sales_sums':daily_sales_sums,'product_sales_sums':product_sales_sums})




def order(request):
    orders = OrderDetail.objects.filter(product__seller=request.user)
    return render(request,'mvdm/order.html',{'orders':orders})