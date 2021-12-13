from django.http import JsonResponse

from group.models import Group


def get_groups(request):
    groups = [
        {
            'group_name': group.group_name,
            'group_direction': group.group_direction,
            'group_size': group.group_size

        }
        for group in Group.objects.all()
    ]

    data = {
        'count': Group.objects.count(),
        'groups': groups,
    }

    return JsonResponse(data)
