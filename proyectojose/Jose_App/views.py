from django.shortcuts import render

def index(request):
    resultado = None  # valor inicial

    if request.method == "POST":
        num1 = int(request.POST.get("num1", 0))
        num2 = int(request.POST.get("num2", 0))
        resultado = num1 + num2  # operación: suma

    return render(request, "Jose_App/index.html", {"resultado": resultado})
