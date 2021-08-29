from django.shortcuts import render, redirect, HttpResponse
from . import rainForest
from .models import *
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    bookList = Book.objects.getTitles()
    bookPrice = Book.objects.getPrice()
    bookImage = Book.objects.getImage()
    mylist = zip(bookList, bookPrice, bookImage)

    context = {
    "bookslist": mylist,     
    }

    return render(request, 'index.html', context)

def loginReg(request):
    return render(request, "loginReg.html")

def description(request):
    return render(request, 'description.html')

def register(request):
    if request.method == "GET":
        return redirect('/loginReg')
    
    errors = User.objects.validate(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/loginReg')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered")
        return redirect('/')
        
    
    
def login(request):
    if request.method == "GET":
        return redirect('/loginReg')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/loginReg')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "You have successfully logged in")
    return redirect('/')
    
    
def logout(request):
    request.session.clear()
    return redirect('/')


