import time

from students.models import Logger


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        method = request.method
        epoch = time.time()

        response = self.get_response(request)

        estimation = round((time.time() - epoch) * 1000, 2)

        if '/admin/' in path:
            Logger.objects.create(method=method, path=path, execution_time=estimation)

        return
