from django.contrib.auth import get_user_model


class AutomaticLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # don't want to login all the time, logs in as first user in db
        request.user = get_user_model().objects.first()
        return self.get_response(request)
