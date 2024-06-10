from django.shortcuts import render,redirect
from clients.forms import LoginForm,CreateUserForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
def login(request):
    if request.user.is_authenticated:
        return redirect('clients:dashboard')
    
    message = None
    if request.method == "POST":
        username_post = request.POST['username']
        password_post = request.POST['password']
        
        user = authenticate(username = username_post, password =password_post)
        if user is not None:
            login_django(request, user )
            return redirect('clients:dashboard')
        else: 
            message = 'Username o Password incorrecto'
    form = LoginForm()
    context = {
        'form':form,
        'message': message, 
        }
    return render(request,'login.html', context )

@login_required(login_url= 'clients:login')
def dashboard(request):
    return render (request,'productos/home.html',{})

@login_required(login_url= 'clients:login')
def logout(request):
    logout_django(request)
    return redirect('clients:login')


def create(request):
    form = CreateUserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)      #Esto nos almacena en la base de datos pero no permite que se retorne el objeto 
            user.set_password( user.password ) #Esto se encarga de encriptar la contraseña que esta en texto plano
            user.save()
            return redirect ('clients:login') 
    context= {
        "form" : form
    }
    
    return render (request,'create.html',context)