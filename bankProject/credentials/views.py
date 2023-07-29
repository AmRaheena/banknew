from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


# Create your views here.
def login(request):
    if request.method == 'POST' :
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('accounts:create_account')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request, "login.html")
def register(request):

    if request.method == 'POST' :
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('credentials:register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                messages.info(request,"User created")
                return redirect('credentials:login')

        else:
            messages.info(request,"Password not matched")
            return redirect('credentials:register')
        return redirect('/')

    return render(request,"register.html")



    #
    # if request.method == 'POST':
    #     username=request.POST['username']
    #     password=request.POST['password']
    #
    # return render(request,'register.html')