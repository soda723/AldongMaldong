from django.shortcuts import render, redirect
# from django.views.decorators.http import require_GET, require_POST
from .models import box_image, Info
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

            # 동물정보 표시
            infodata = Info.objects.get(name = what)
            print(infodata)
            context['infodata'] = infodata

            return render (request, 'mainapp/search_result.html', context)

        else:
            #이미지가 업로드 되지 않으면 다시 화면 보여줌
            redirect('mainapp:go_search')

        
    else :
        #get 요청(잘못된요청) -> main 페이지로
        return redirect('mainapp:main')
    