from django.urls import path

from web import views
from web import recipeViews
urlpatterns=[
    path('',views.main_page),
    path('recipe/list/',recipeViews.recipe_list)
]