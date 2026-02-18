from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Q
from report import report_genrate

import os
from django.core.files.storage import default_storage
from django.conf import settings

# Create your views here.

def home(request):
    return render(request,"home1.html")



def regestration(request):
    if request.method =="POST":
        name =request.POST.get("first_name")
        username =request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj = User.objects.filter(Q(email = email),Q(username=username))

        if user_obj.exists():
            messages.error(request,"ERROR: user exit already")
            return redirect("/regestration")
        user_dt = User.objects.create(
            first_name = name,
            username = username,
            email = email
        )
        user_dt.set_password(password)
        user_dt.save()
        messages.success(request,"SUCCESS: acount created")
        return redirect("/login")
    return render(request,"reg.html")

def login_page(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = User.objects.filter(username = username)
        if not user_obj.exists():
            messages.error(request,"ERROR: user not exits")
            return redirect("/regestration")
        user_ob = authenticate(username = username,password = password)

        if not user_ob:
            messages.error(request,"ERROR: invalid credintials")
            return redirect("/login.html")
        login(request,user_ob)
        return redirect("/")
    return render(request,"login.html")

def logout_page(request):
    logout(request)
    messages.error(request,"succes : user is logout")
    return redirect("/")


@login_required(login_url="/login/")
def report_maker(request):
    if request.method =="POST":
        #image = request.POST.get("image")
        image = request.FILES.get("image")
        temp_image_path = default_storage.save('temp_image.png', image)
        temp_image_full_path = os.path.join(settings.MEDIA_ROOT, temp_image_path)
        print(temp_image_path)
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        report_genrate(temp_image_path,name,age,gender)
        messages.error(request,"succes : user report is sent.......")
        return redirect("report_gen")
    return render(request,"form.html")


def about_page(request):
    return render(request,"about.html")


def report_genr(request):
    return render(request,"report.html")




















