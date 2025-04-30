from django.shortcuts import render,redirect
from django.http import JsonResponse

from web import foodModels


def food_list(request):
    return render(request,"food/list.html")

def food_list_vue(request):
    '''
      if(page==null)
          page="1"
      int curpage=Integer.parseInt(page)
    '''
    try:
        page=request.GET['page']
    except Exception as e:
        page="1"
    curpage=int(page)

    foodList, totalpage = foodModels.foodListData(curpage)
    BLOCK = 10
    startPage = ((curpage - 1) // BLOCK * BLOCK) + 1
    endPage = ((curpage - 1) // BLOCK * BLOCK) + BLOCK

    # startPage=int(startPage)
    # endPage=int(endPage)
    if endPage > totalpage:
        endPage = totalpage

    rd = []
    for r in foodList:
        rdata = {"fno": r[0], "name": r[1], "poster": r[2]}
        rd.append(rdata)
    recipe_data = {
        "fd": rd,
        "curpage": curpage,
        "totalpage": totalpage,
        "startPage": startPage,
        "endPage": endPage
    }
    return JsonResponse(recipe_data)





