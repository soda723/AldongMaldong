from django.shortcuts import render, redirect
from .models import RescueCenter
from django.core.paginator import Paginator
# Create your views here.

def searchRC(request):

    context = {}
    page = request.GET.get('page', 1) #페이지 디폴트 값1

    contents = RescueCenter.objects.all()
    if request.method == "POST":
        #검색한다
        
        regions = request.POST.getlist('regions[]')
        #regions  ['전체', '서울', '전남']
        print(regions)
        if '전체' in regions : 
            context['results'] = contents
            context['regions'] = ["전체"]
            return render(request, 'sub1app/searchRc.html', context)

        else :
            #지역 검색
            results = contents.filter(XXX='임시')
            for reg in regions:
                temp = contents.filter(XXX=reg)
                results  = results.union(temp)
            context['results'] = results
            context['regions'] = regions
            return render(request, 'sub1app/searchRc.html', context)

    else :
        #전체 리스트 보여주기
        paginator = Paginator(contents, 10)#페이지 당 10개씩
        page_obj = paginator.get_page(page)
        context['results'] = page_obj
        context['regions'] = ["전체"]
        return render(request, 'sub1app/searchRc.html', context)


def center_info(request, obj_pk):
    context={}

    contents = RescueCenter.objects.get(pk=obj_pk)
    context['data'] = contents

    return render(request, 'sub1app/center_info.html', context)

