from django.shortcuts import render,redirect
from tracker.models import Contact
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def home_page(request,*args, **kwargs):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST['message']
        contact=Contact.objects.create(name=name,email=email,message=message)
        contact.save()
        return redirect('home')
    return render(request,'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)  # Creates a hashed password
        user.save()

        messages.success(request, "Registration successful. Please login.")
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method=='POST':
      username=request.POST['username']
      password=request.POST['password']
      user=authenticate(request,username=username,password=password)
      if user is not None :
          login(request,user)
          messages.success(request,'Login Successful')
          return redirect('home')
      else :
          messages.error(request,'Invalid Login Credentials')
          return render(request,'login.html')
    return render(request,'login.html')

def logout_view(request):
    user=request.user
    logout(request)
    messages.success(request,'Logout Successfully')
    return redirect('home')
