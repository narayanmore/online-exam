from django.urls import path
from login import views
urlpatterns=[
    path('regi/',views.registration),
    path('login/',views.loginfun),
]