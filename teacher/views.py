import random

from django.forms import model_to_dict
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from faker import Faker

from teacher.forms import TeacherForm
from teacher.models import Teacher


def get_teachers(request):
    queryset = Teacher.objects.all()
    return render(request, 'teacher/index.html',
                  context={'teachers': queryset})


def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    if request.method == 'GET':
        form = TeacherForm(instance=teacher)

        return render(request, 'teacher/edit.html', context={'form': form})

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect(reverse('teacher:list'))

        return render(request, 'teacher/edit.html', context={'form': form})

    return HttpResponse(status=405)


@require_http_methods(['GET', 'POST'])
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teacher:list'))

    return render(request, 'teacher/edit.html')


@require_http_methods(['GET', 'POST'])
def create_teachers(request):

    if request.method == 'GET':
        fake = Faker()

        data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'age': random.randint(18, 65),
        }

        form = TeacherForm(initial=data)

        return render(request, 'teacher/create.html',
                      context={'form': form})

    form = TeacherForm(request.POST)

    if form.is_valid():
        form.save()

        return HttpResponseRedirect(reverse('teacher:list'))

    return HttpResponse(str(form.errors), status=400)
