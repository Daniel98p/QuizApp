from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Question


class WelcomeView(View):
    greeting = "Welcome in the main page"

    def get(self, request):
        return HttpResponse(self.greeting)


class Index(View):
    def get(self, request):
        latest_question = Question.objects.last()
        context = {"latest_question": latest_question}
        return render(request, "quiz_app/index.html", context=context)
