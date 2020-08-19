from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, Quiz
from .forms import QuizForm


@login_required
def select_quiz(request):
    quizzes = Quiz.objects.all()
    context = {"quizzes": quizzes}
    return render(request, 'quiz_app/selector.html', context=context)


@login_required
def render_quiz(request, quiz_id):
    questions = Question.objects.filter(quiz_id=quiz_id)
    quiz = Quiz.objects.get(pk=quiz_id)
    questions_id = [question.id for question in questions]
    answers = Answer.objects.filter(question_id__in=questions_id)
    if request.method == 'POST':
        form = QuizForm(request.POST, answers=answers, questions=questions)
        if form.is_valid():
            request.session["question_1"] = form.cleaned_data["question_1"]
            request.session["question_2"] = form.cleaned_data["question_2"]
            request.session["question_3"] = form.cleaned_data["question_3"]
            return redirect('quiz_app:show-results', quiz_id=quiz_id)
    else:
        form = QuizForm(answers=answers, questions=questions)
    context = {"questions": questions, "form": form, "quiz": quiz}
    return render(request, "quiz_app/index.html", context=context)


@login_required
def show_results(request, quiz_id):
    questions = Question.objects.filter(quiz_id=quiz_id)
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
    print(questions_id)
    print(selected_choice_obj_1.question_id)
    good_answers = 0
    for question, choice in zip(questions_id, selected_choices_question_id):
        if question == choice:
            good_answers += 1
    context = {"questions_id": questions_id, "selected_choices_id": selected_choices_question_id,
               "good_answers": good_answers}
    return render(request, "quiz_app/result.html", context=context)
