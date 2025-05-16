from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create-todo/',views.create_todo,name='create_todo'),
    path('edit-todo/<int:pk>',views.edit_todo,name='edit_todo')
]
