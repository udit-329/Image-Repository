from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import image
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension
from django.core.validators import FileExtensionValidator
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.
def index(request):
    images = image.objects.filter(private=False)
    return render(request=request, template_name="index.html", context={'images': images})

def private(request):
    images = image.objects.filter(private=True, owner=request.user)
    return render(request=request, template_name="private.html", context={'images': images})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Account successfully created!")
            login(request, user)
            return redirect("main:index")
        else:
            for msg in form.error_messages:   
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

    form = UserCreationForm
    return render(request=request, template_name="register.html", context={"form":form})

def check_validation_error(request, new_image):
    try:
        new_image.full_clean()
    except ValidationError as e:
        picture_error = e.message_dict.get('picture')
        for msg in picture_error:
            messages.error(request, f"{msg}")
    else:
        new_image.save()

def upload_image(request):
    pic = request.FILES['image']
    name_pic = pic.name
    
    if request.user.is_authenticated:
        user = request.user
        new_image = image(picture=pic, owner=user, name=name_pic)
    else:
        new_image = image(picture=pic, name=name_pic)

    check_validation_error(request, new_image)
    
    return redirect("main:index")

def search(request):
    
    search = request.POST.get("search")
    
    images = image.objects.filter(Q(name__icontains=search) | Q(owner__username__icontains=search))
    
    return render(request=request, template_name="index.html", context={'images': images, 'line': search})

def upload_image_private(request):
    pic = request.FILES['image']
    name_pic = pic.name
    
    if request.user.is_authenticated:
        user = request.user
        new_image = image(picture=pic, owner=user, name=name_pic, private=True)
    
    check_validation_error(request, new_image)

    return redirect("main:private")

def logout_account(request):
    logout(request)
    return redirect("main:index")

def login_account(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Logged in successfully!")
                return redirect("main:index")
            else:
                messages.error(request, f"Invalid username or password")
        else:
            messages.error(request, f"Invalid username or password")
        
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form":form})

def delete_image(request, pk):
    if request.method == 'POST':
        im = image.objects.get(pk=pk)
        im.delete()
    return redirect('main:index')