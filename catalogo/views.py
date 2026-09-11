from django.shortcuts import render

def mostrar_productos(request):

    productos = [

        
    ]

    return render(request, 'index.html', {"productos": productos})