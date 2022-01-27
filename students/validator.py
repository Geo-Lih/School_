from django.core.exceptions import ValidationError


def validate_phone(number):
    operators_list = ['096', '097', '095', '066', '068']
    if len(number) != 13:
        raise ValidationError(f'{number} length is not correct ')

    if not str.isdigit(number[1:]):
        raise ValidationError(f'{number} is not correct enter only numbers')

    if number[0:3] != '+38':
        raise ValidationError(f'{number} telephone code is not correct ')

    if number[3:6] not in operators_list:
        raise ValidationError(f'{number} operator cod  is not correct ')
