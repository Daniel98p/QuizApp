from django.http import HttpResponse
from django.views import View


class WelcomeView(View):
    greeting = "Welcome in the main page"

    def get(self, request):
        return HttpResponse(self.greeting)
