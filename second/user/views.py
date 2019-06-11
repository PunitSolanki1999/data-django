from django.shortcuts import render,redirect
from .models import User
from .forms import Data_signup_form,User_signin
# Create your views here.
def logout(request,**kwargs):
    del request.session['username']
    return render(request,"user/interface.html",{})

def logged(request,**kwargs):
    if request.session.has_key('username'):
        user = request.session['username']
        return render(request,"user/logged.html",{'user':user})
    else:
        return user_login(request)

def interface(request):
    return render(request,"user/interface.html",{})

def data_view(request,*args,**kwargs):
    form = Data_signup_form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()


    context = {
        'form': form,
    }
    return render(request,"user/signup.html",context)

def user_login(request,*args,**kwargs):
    form = User_signin(request.POST or None)
    password_not_available = False
    username_not_available = False
    if request.method == 'POST':
        if form.is_valid():
            data = request.POST.copy()
            username = data.get('username')
            password = data.get('password')
            try:
                user = User.objects.get(username=username)
                if user:
                    if(user.username == username and user.password == password):
                        request.session['username'] = username
                        return redirect("user:logged")
                    else:
                        password_not_available = True
            except User.DoesNotExist:
                username_not_available = True
        

    context = {
        'form': form,
        'username_not_available' : username_not_available,
        'password_not_available' : password_not_available,
    }
    return render(request,"user/signin.html",context)