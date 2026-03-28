from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('addexp/',views.addForm,name='add_exp'),
    path('listexp/',views.listExp,name='list_exp'),
    path('delete/<int:id>/',views.deleteExp,name='delete_exp'),
    path('update/<int:id>/',views.updateExp,name='update_exp'),
]
