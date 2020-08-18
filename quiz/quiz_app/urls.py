from django.urls import path
from .views import select_quiz, render_quiz, show_results

urlpatterns = [
    path('', select_quiz, name='select-quiz'),
    path('1/', render_quiz, name="render-quiz"),
    path('1/results/', show_results, name='show-results'),
              ]
