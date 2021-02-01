from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name="detail"),
    path('complete/<todo_id>', views.complete_todo, name='complete'),
    path('deletecomplete', views.delcompleted, name = 'deletecomplete'),
    path('delall/', views.delall, name='deleteall'),
    path('notcompleted/<int:todo_id>', views.notcompleted, name='notcompleted')
]
