from django.urls import path

from web import views
from web import recipeViews
from web import foodViews
urlpatterns=[
    path('',views.main_page),
    path('recipe/list/',recipeViews.recipe_list),
    path('recipe/detail_before/',recipeViews.recipe_before),
    path('recipe/detail/',recipeViews.recipe_detail),
    path('food/list/',foodViews.food_list),
    path('food/list_vue/',foodViews.food_list_vue)
]