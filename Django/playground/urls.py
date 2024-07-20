# from django.contrib import admin
from django.urls import path
from . import views

# url configuration
urlpatterns = [
    path('hello/', views._say_Hello_),
    path('by/', views.__Say_By__ ),
    path('presentation/', views._Presentation_ ) 
]

# [print(item) for item in urlpatterns]
# tool_bar : 15
# 12
