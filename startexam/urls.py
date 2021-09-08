from django.urls import path
from startexam.views import*
urlpatterns=[
    path('startexam/',startexam),
    path('fun_logout/',fun_logout)
]