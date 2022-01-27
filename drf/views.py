from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from drf.serializers import StudentSerializer, GroupSerializer, TeacherSerializer, StudentDetailSerializer, \
    GroupDetailsSerializer
from group.models import Group
from students.models import Student
from teacher.models import Teacher


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentDetailSerializer

    def get_object(self):
        return get_object_or_404(Student, pk=self.kwargs.get('student_id'))


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupDetailsSerializer

    def get_object(self):
        return get_object_or_404(Group, pk=self.kwargs.get('group_id'))


class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
