from django.shortcuts import render, redirect

# Create your views here.

def main(request):
    return render(request, 'mainapp/main.html')

def go_search(request):
    return render(request, 'mainapp/go_search.html')
