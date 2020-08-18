from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Question, Answer
from .forms import QuizForm


def select_quiz(request):
    question = Question.objects.last()
    context = {"question": question}
    return render(request, 'quiz_app/selector.html', context=context)


def render_quiz(request):
    questions = Question.objects.all()
    answers = Answer.objects.all()
    if request.method == 'POST':
        form = QuizForm(request.POST, answers=answers, questions=questions)
        if form.is_valid():
            request.session["question_1"] = form.cleaned_data["question_1"]
            request.session["question_2"] = form.cleaned_data["question_2"]
            request.session["question_3"] = form.cleaned_data["question_3"]
            return redirect('/quiz_app/1/results/')
    else:
        form = QuizForm(answers=answers, questions=questions)
    context = {"questions": questions, "form": form}
    return render(request, "quiz_app/index.html", context=context)


def show_results(request):
    questions = Question.objects.all()
    questions_id = [question.id for question in questions]
    try:
        selected_choice_1 = request.session.get('question_1')
        selected_choice_2 = request.session.get('question_2')
        selected_choice_3 = request.session.get('question_3')
    except KeyError:
        return HttpResponse("There is no choice")
    selected_choice_obj_1 = Answer.objects.get(answer_text=selected_choice_1)
    selected_choice_obj_2 = Answer.objects.get(answer_text=selected_choice_2)
    selected_choice_obj_3 = Answer.objects.get(answer_text=selected_choice_3)
    selected_choices_question_id = [selected_choice_obj_1.question_id, selected_choice_obj_2.question_id,
                                    selected_choice_obj_3.question_id]
    good_answers = 0
    for question, choice in zip(questions_id, selected_choices_question_id):
        if question == choice:
            good_answers += 1
    context = {"questions_id": questions_id, "selected_choices_id": selected_choices_question_id,
               "good_answers": good_answers}
    return render(request, "quiz_app/result.html", context=context)
