from django.urls import path

from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.get_teachers, name='list'),
    path('<int:teacher_id>/edit/', views.edit_teacher, name='edit'),
    path('create/', views.create_teachers, name='create'),
    path('<int:teacher_id>/delete/', views.delete_teacher, name='delete'),
]
