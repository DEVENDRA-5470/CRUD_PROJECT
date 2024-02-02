from django.urls import path
from .views import *
urlpatterns=[
    path("",home,name="home"),
    path("account",account,name="account"),
    path("delete/<int:id>/",delete,name="delete"),
    path("success/",success,name="success"),
    path("update/<int:id>/",update,name="update"),
]