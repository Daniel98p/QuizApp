from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.QuestionList.as_view()),
    path('quiz/', views.QuizList.as_view()),
    path('answer/', views.AnswerList.as_view()),
]
