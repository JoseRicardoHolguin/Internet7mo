from django.shortcuts import render

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
    return render(request, "Jose_App/random_number.html", {"numero": numero_aleatorio})

def saludo(request, nombre):
    return render(request, "Jose_App/saludo.html", {"nombre": nombre.capitalize()})