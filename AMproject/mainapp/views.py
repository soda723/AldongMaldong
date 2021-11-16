from django.shortcuts import render, redirect
# from django.views.decorators.http import require_GET, require_POST


# Create your views here.

def main(request):
    return render(request, 'mainapp/main.html')

def go_search(request):
    return render(request, 'mainapp/go_search.html')

# @require_POST
def search_result(request):
    
    if request.method == 'POST':
        if 'image' in request.FILES:
            pass
        else:
            redirect('mainapp:go_search')

        return render (request, 'mainapp/search_result.html')
    else :
        #get 요청 -> main 페이지로
        return redirect('mainapp:main')
    