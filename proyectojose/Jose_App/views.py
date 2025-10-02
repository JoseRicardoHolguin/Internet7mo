from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Task

tasks = ["foo", "bar", "baz"]

def suma(request):
    resultado = None  # valor inicial

    if request.method == "POST":
        num1 = int(request.POST.get("num1", 0))
        num2 = int(request.POST.get("num2", 0))
        resultado = num1 + num2  # operación: suma

    return render(request, "Jose_App/suma.html", {"resultado": resultado})

def ruido(request):
    return render(request, "Jose_App/ruido.html")

def random_number(request):
    import random
    numero_aleatorio = random.randint(1, 100)
    return render(request, "Jose_App/random.html", {"numero": numero_aleatorio})

def saludo(request, nombre):
    return render(request, "Jose_App/saludo.html", {"nombre": nombre.capitalize()})

def index(request):
    return render(request, "Jose_App/index.html")

def about(request):
    return render(request, "Jose_App/about.html")

def task_index(request):
    return render(request, "Jose_App/task_index.html", 
                  {"tasks": tasks})

def tasks_add(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task:
            tasks.append(task)
        return HttpResponseRedirect (reverse("task_index"))
    return render(request, "Jose_App/task_index.html")

def tasks_admin_list(request):
    task = Task.objects.all().order_by("created_at")
    return render(request, "Jose_App/task_admin_list.html", {"tasks": task})    



    
