

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from product.models import Seller

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

            # return render(request,'defaultlogin.html',{'username':username})
            return redirect('/')
            # return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('/accounts/login')
    else:
        return render(request, 'registration/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        phone=request.POST['phone']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('/accounts/register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already taken")

                return redirect('/accounts/register')
            else:

                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                password=password1, email=email)
              
                user.save()

                reg=Seller(user=user,phone=phone)
                reg.save()
               
                messages.success(request, "Registration successfull")
                return redirect('/accounts/login')
        else:
            messages.success(request, "password incorrect")
        
            return redirect('/accounts/register')

       
           
          

        return redirect('/')
    else:

        return render(request, 'registration/register.html')
def profile(request):
    data=Seller.objects.get(user__id=request.user.id)
    context={
        'data':data
    }
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone=request.POST['phone']

        usr=User.objects.get(id=request.user.id)
        usr.first_name=first_name
        usr.last_name=last_name
        usr.username=username
        usr.email=email
        usr.save()
        data.phone=phone
        data.save()

        messages.info(request,"Profile Updated Successfully")
    return render(request,"profile.html",context)
    