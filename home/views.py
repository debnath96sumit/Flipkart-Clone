from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from home.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == "POST":
        number = request.POST['number']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        if User.objects.filter(username = firstname).exists():
            messages.error(request, "User already exists")
            return redirect('/signup')

        user_obj = User.objects.create(
            username = firstname,
            first_name = firstname,
            last_name = lastname,
            email = email
        )
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, "Account created successfully")
        return redirect("/")
        # data = userdata(number=number, email = email, firstname=firstname, lastname=lastname, password=password)
        # data.save()
        # return redirect("/")
    return render(request, "fk_signup.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # if not User.objects.filter(username = username).exists():
        #     return render(request, "error.html")

        user_obj = authenticate(username = username, password = password)

        if user_obj:
            login(request, user_obj)
            return redirect("/index")
        messages.error(request, "Invalid credentials")
        return redirect('/')
    return render(request, "fk_login.html")

def logout_page(request):
    logout(request)
    return redirect('/')

@login_required(login_url= '/')
def index(request):
    allproduct = product.objects.all()
    params = {'allproduct': allproduct}
    return render(request, "fk-index.html", params)

@login_required(login_url= '/')
def contacts(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        desc = request.POST['desc']
        mydata = contact(email=email, name=name, desc=desc)
        mydata.save()
        
    return render(request, "fk-contact.html")

def details(request, id):
    myprod = product.objects.filter(id=id)
    return render(request, "detail.html", {'product': myprod[0]})

@login_required(login_url= '/')
def mycart(request):
    return render(request, "cart.html")
    
@login_required(login_url= '/')
def search(request):
    query = request.GET['query']
    allproduct = product.objects.filter(name__icontains = query)
    return render(request, 'fk_search.html', {'allproduct': allproduct})