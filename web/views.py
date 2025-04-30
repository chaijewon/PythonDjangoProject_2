from django.shortcuts import render,redirect
# Vuex
'''
    사용자 요청 => DispatcherServlet => Model(@Controller) = ViewResolver
        |
    사용자 요청 => urls.py => views.py <=> models.py
                               |
                            화면 이동 (html)
    urls.py : @GetMapping , @PostMapping , @RequestMapping
    views.py : @Controller , @RestController 
    models.py : @Repository 
                                                        
'''
from web import models
def main_page(request):
    recipe_list,food_list=models.mainData()
    '''
     [
       (),(),()...
     ]
     데이터 전송은 dict만 가능 {키:값}
     model.addAttribute("list",list)
     Map map=new HashMap()
     map.put("curpage",curpage)
     map.put("totalpage",totalpage)
     map.put("list",list)
     model.addAllAttribute(map)
    '''
    rd=[]
    for r in recipe_list:
        rdata={"no":r[0],"title":r[1],"poster":r[2],"chef":r[3]}
        rd.append(rdata)

    fd = []
    for r in food_list:
        rdata = {"fno": r[0], "name": r[1], "poster": r[2]}
        fd.append(rdata)
    # Cookie
    return render(request,'main/home.html',{
        "rd":rd,
        "fd":fd
    })
# Create your views here.
