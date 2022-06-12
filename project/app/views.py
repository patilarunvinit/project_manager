
from django.shortcuts import render,redirect
from .models import login1,data

from .serializer import dataserializer


# Create your views here.

def login(request):
    info=loginapi(request)
    if info:
       aa=info[0]
       if aa=="admin":
          return redirect('http://127.0.0.1:8000/ad/')
       elif aa=="man":
          return redirect('http://127.0.0.1:8000/man/')
       elif aa=="dev":
          email=info[1]
          print(email)
          request.session['email'] = email
          return redirect('http://127.0.0.1:8000/dev/')
       else:
          print("wrong")
    return render(request, "login.html")

def admin(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        data.objects.create(name=name)
    return render(request, "admin.html")

def man(request):
    data1=data.objects.all()
    if request.method == 'POST':
        name=request.POST.get("name")
        task=request.POST.get("task")
        asignto = request.POST.get("asignto")
        review = request.POST.get("review")
        status = request.POST.get("status")
        if task:
            print("yes")
            data.objects.filter(name=name).update(task=task, asignto=asignto)
        else:
            print("no")
            data.objects.filter(name=name).update(review=review, status=status)

    return render(request, "man.html",{'data1': data1})

def dev(request):
    data1 = data.objects.all()
    email = request.session.get('email')
    if request.method == 'POST':
        name=request.POST.get("name")
        status=request.POST.get("status")
        data.objects.filter(name=name).update(status=status)
    return render(request, "dev.html", {'email':email,'data1':data1})



def loginapi(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        option= request.POST.get("cars")

        try:
            a=login1.objects.get(email=email,password=password,option=option)
            if a.email is not None and a.password is not None and a.option =="admin":
                print("admin")
                email=a.email
                out="admin"
                return [out,email]

            elif a.email is not None and a.password is not None and a.option =="man":
                print("man")
                email = a.email
                out = "man"
                return [out, email]

            elif a.email is not None and a.password is not None and a.option =="dev":
                print("dev")
                email = a.email
                out = "dev"
                return [out, email]


        except:
            return 0