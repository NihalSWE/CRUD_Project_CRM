from django.shortcuts import redirect, render
from .forms import CreateUserForm,LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import ClientData
# Create your views here.
def home(request):
    return render(request, 'client/home.html')


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form
    }

    return render(request,'client/register.html',context)


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:

                auth.login(request, user)
                return redirect('/dashboard')


    context = {
        'form' : form
    }

    return render(request,'client/login.html',context)



@login_required(login_url='login')
def dashboard(request):
    my_data = ClientData.objects.all()
    context={'datas':my_data}




    return  render(request,"client/dashboard.html",context)


def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def add(request):
    return render (request,"client/create.html")