import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from faker import Faker

from group.forms import GroupForm
from group.models import Group


def get_groups(request):
    queryset = Group.objects.all()
    return render(request, 'group/index.html',
                  context={'groups': queryset})


def edit_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'GET':
        form = GroupForm(instance=group)

        return render(request, 'group/edit.html', context={'form': form})

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect(reverse('group:list'))

        return render(request, 'group/edit.html', context={'form': form})

    return HttpResponse(status=405)


@require_http_methods(['GET', 'POST'])
def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('group:list'))

    return render(request, 'group/edit.html')


@require_http_methods(['GET', 'POST'])
def create_groups(request):

    if request.method == 'GET':
        fake = Faker()

        data = {
            'group_name': fake.license_plate(),
            'group_direction': fake.language_name(),
            'group_size': random.randint(6, 20),
        }

        form = GroupForm(initial=data)

        return render(request, 'group/create.html',
                      context={'form': form})

    form = GroupForm(request.POST)

    if form.is_valid():
        form.save()

        return HttpResponseRedirect(reverse('group:list'))

    return HttpResponse(str(form.errors), status=400)
