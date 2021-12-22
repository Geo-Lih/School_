from django.urls import path

from . import views

app_name = 'students'

urlpatterns = [
    path('', views.get_students, name='list'),
    path('<int:student_id>/edit/', views.edit_student,
         name='edit'),
    path('create/', views.create_students, name='create'),
    path('<int:student_id>/delete/', views.delete_student, name='delete'),
]
