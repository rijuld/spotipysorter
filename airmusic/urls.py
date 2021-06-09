
from django.urls import path
from . import views

app_name="airmusic"
urlpatterns = [
    path("", views.index, name="index"),
    path("page1", views.page1, name="page1"),
    path("page2", views.page2, name="page2"),
    path("page3", views.page3, name="page3"),
    path("searchresult", views.searchresult, name="searchresult"),
    path("page1add", views.page1add, name="page1add"),
    path("page1remove", views.page1remove, name="page1remove"),
    path("page1textarea", views.page1textarea, name="page1textarea"),
    path("all", views.all, name="all"),
    path("colors", views.colors, name="colors"),
   
]
