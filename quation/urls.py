from django.urls import path
from quation import views
urlpatterns=[
    path('',views.quations),
]