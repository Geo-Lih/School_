# flake8: noqa
from django.urls import include, path
from rest_framework import routers
from drf import views

# router = routers.DefaultRouter()
# router.register(r'students', views.StudentList)
# router.register(r'students/<int:student_id>', views.StudentDetails)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'teachers', views.TeacherViewSet)

app_name = 'drf'


urlpatterns = [
    # path('', include(router.urls)),
    path('students/', views.StudentList.as_view(), name='StudentList'),
    path('students/<int:student_id>', views.StudentDetails.as_view(), name='StudentDetails'),
    path('groups/', views.GroupList.as_view(), name='GroupList'),
    path('groups/<int:group_id>', views.GroupDetails.as_view(), name='GroupDetails'),
    path('teachers/', views.TeacherList.as_view(), name='TeacherList')
]
