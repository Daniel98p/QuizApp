from django.urls import path
from .views import select_quiz, render_quiz, show_results, show_ranking


app_name = "quiz_app"
urlpatterns = [
    path('', select_quiz, name='select-quiz'),
    path('<int:quiz_id>/', render_quiz, name="render-quiz"),
    path('<int:quiz_id>/results/', show_results, name='show-results'),
    path('ranking/', show_ranking, name='show-ranking'),
              ]
