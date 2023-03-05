from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Orphan
from django.contrib import messages
from .forms import SignUpForm
from .forms import EditForm, EditCaseInfoForm
# Create your views here.
def index(request):
    return render(request, 'orphan/index.html',)

def about(request):
    return render(request, 'orphan/about.html',)

def causes(request):
    return render(request, 'orphan/causes.html',)

def event(request):
    return render(request, 'orphan/event.html',)

def blog(request):
    return render(request, 'orphan/blog.html',)

def panel(request):
    mydata = Orphan.objects.all().values()
    context = {'mymembers': mydata}
    return render(request, 'orphan/panel.html', context)


def single(request):
    return render(request, 'orphan/single.html',)

def service(request):
    return render(request, 'orphan/service.html',)

def team(request):
    return render(request, 'orphan/team.html',)

def donate(request):
    return render(request, 'orphan/donate.html',)

def volunteer(request):
    return render(request, 'orphan/volunteer.html',)

def contact(request):
    return render(request, 'orphan/contact.html',)

def admin(request):
    return render(request, 'orphan/admin.html',)

def response(request):
    return render(request, 'orphan/response.html',)



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.save()
            

            return redirect('home')
    else:
        form = SignUpForm()
    
    return render(request, 'orphan/register.html', {'form': form})

def admin_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("panel")
            else:
                messages.error(request, "user does not exist or wrong password")

    form = AuthenticationForm()

    return render(request, 'orphan/admin_login.html', context={"login_form": form})


def donate_now(request, pk):
    obj = Orphan.objects.get(id=pk)
    form = EditCaseInfoForm()
    if request.method == 'POST':
        form = EditCaseInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, ' details updated successfully.')
            return redirect('response')

    context = {'form': form}
    return render(request, 'orphan/donate_now.html', context)

