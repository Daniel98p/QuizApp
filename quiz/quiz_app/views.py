from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Question, Answer
from .forms import QuizForm


class WelcomeView(View):
    greeting = "Welcome in the main page"

    def get(self, request):
        return HttpResponse(self.greeting)


def render_quiz(request):
    latest_question = Question.objects.last()
    answers = Answer.objects.all()
    if request.method == 'POST':
        form = QuizForm(request.POST, answers=answers)
        if form.is_valid():
            request.session["choice"] = form.cleaned_data["choice"]
            return redirect('/quiz_app/1/results/')
    else:
        form = QuizForm(answers=answers)
    context = {"latest_question": latest_question, "form": form}
    return render(request, "quiz_app/index.html", context=context)


def show_results(request):
    question = Question.objects.last()
    try:
        selected_choice = request.session.get('choice')
    except KeyError:
        return HttpResponse("There is no choice")
    selected_choice_obj = Answer.objects.get(answer_text=selected_choice)
    context = {"question": question, "selected_choice_obj": selected_choice_obj}
    return render(request, "quiz_app/result.html", context=context)
