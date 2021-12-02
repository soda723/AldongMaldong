from django.shortcuts import render, redirect
# from django.views.decorators.http import require_GET, require_POST
from .models import box_image
from yolo_object_detection.yolo_detection import result_str 

# Create your views here.

def main(request):
    return render(request, 'mainapp/main.html')

def go_search(request):
    return render(request, 'mainapp/go_search.html')

# @require_POST
def search_result(request):
    context={}
    
    if request.method == 'POST':
        if 'image' in request.FILES:
            imagee=request.FILES['image']
            new_image=box_image(image = imagee)
            new_image.save()
            fname = imagee.name
            file_path = f"./media/userimg/{fname}"
            context['file_path'] = file_path

            #결과값 받아오기
            what = result_str(file_path)
            context['what'] = what
            #사용후 파일 지우기
            #new_image.delete()
            return render (request, 'mainapp/search_result.html', context)

        else:
            redirect('mainapp:go_search')

        
    else :
        #get 요청 -> main 페이지로
        return redirect('mainapp:main')
    