from django.urls import path

from . import views

app_name = 'group'
urlpatterns = [
    path('', views.get_groups, name='list'),
    path('<int:group_id>/edit/', views.edit_group, name='edit'),
    path('create/', views.create_groups, name='create'),
    path('<int:group_id>/delete/', views.delete_group, name='delete'),
]
