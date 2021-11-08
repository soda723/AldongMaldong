from django.shortcuts import render, redirect
from .models import RescueCenter
# Create your views here.

def searchRC(request):

    context = {}

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
        context['results'] = contents
        context['regions'] = ["전체"]
        return render(request, 'sub1app/searchRc.html', context)

