from django.shortcuts import render

def show_index(request):
    return render(request, "mydj/templates/mydj/index.html")