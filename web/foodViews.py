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

'''
fno,name,poster,address,phone,
                   time,theme,content,type,parking
'''
def food_detail(request):
    fno=request.GET['fno']
    return render(request,"food/detail.html",{
        "fno":fno
    })

def food_detail_vue(request):
    fno=request.GET['fno']
    # String fno=request.getParameter("fno")
    detail=foodModels.foodDetailData(int(fno))
    '''
      Collection (자바) 
      list [1,2,3,4..]
      set  {1,2,3,4,5..}
      tuple (1,2,3,4,5..)
      dict {"key":"value"}
    '''
    fd={
        "fno": detail[0],
        "name": detail[1],
        "poster": detail[2],
        "address": detail[3],
        "phone": detail[4],
        "time": detail[5],
        "theme": detail[6],
        "content": detail[7],
        "type": detail[8],
        "parking": detail[9]
    }

    return  JsonResponse(fd)






