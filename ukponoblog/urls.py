from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path("blog/<str:pk>",views.blog,name="blog")
]
