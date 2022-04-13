from django.urls import path

from .views import categoriesList, categoriesDetail


urlpatterns = [
    path('', categoriesList, name='categories'),
    path('<str:category_slug>/', categoriesDetail, name='categories-detail'),
]
