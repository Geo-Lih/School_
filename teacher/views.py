from django.http import JsonResponse

from teacher.models import Teacher


def get_teachers(request):
    teachers = [
        {
            'first_name': teacher.first_name,
            'last_name': teacher.last_name,
            'age': teacher.age

        }
        for teacher in Teacher.objects.all()
    ]

    data = {
        'count': Teacher.objects.count(),
        'teachers': teachers,
    }

    return JsonResponse(data)
