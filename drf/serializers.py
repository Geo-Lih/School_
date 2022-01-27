from rest_framework import serializers

from group.models import Group
from students.models import Student
from teacher.models import Teacher


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'age']


class StudentDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age']


class StudentNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'group_name', 'group_direction', 'group_size']


class GroupDetailsSerializer(serializers.HyperlinkedModelSerializer):
    students = StudentNestedSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ['group_name', 'students']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'age']
