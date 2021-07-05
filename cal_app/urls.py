from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home1'),
    path('<str:month>/<int:year>/',views.index,name='index'),
]