import random

from django.http import HttpResponse, JsonResponse

from faker import Faker

from students.models import Student


def index(request):
    return HttpResponse('<h1> Wellcome to my HOME WORK</h1>')


def get_students(request):
    students = [
       {
        'id': student.id,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'age': student.age
       }
       for student in Student.objects.all()
    ]
    data = {
        'count': Student.objects.count(),
        'students': students,
    }
    return JsonResponse(data)


def create_students(request, age):
    fake = Faker()

    data = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'age': age,
    }

    student = Student(**data)
    student.save()

    return JsonResponse(data)


def generate_students(request):

    fake = Faker()
    gen_students = {
                 'count': request.GET.get('count')
    }

    try:
        gen = int(gen_students['count'])
        if 100 < gen or gen < 0:
            raise ValueError
    except KeyError:
        pass
    student_list = []
    for _ in range(gen):
        data = {
             'first_name': fake.first_name(),
             'last_name': fake.last_name(),
             'age': random.randint(1, 92),
        }
        student_list.append(data)
        student = Student(**data)
        student.save()

    return HttpResponse(student_list)
