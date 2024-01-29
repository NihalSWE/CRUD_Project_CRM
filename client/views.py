from django.shortcuts import redirect, render
from .forms import CreateUserForm,LoginForm
# Create your views here.
def home(request):
    return render(request, 'client/home.html')


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect()

    context = {
        'form': form
    }






    return render(request,'client/register.html',context)