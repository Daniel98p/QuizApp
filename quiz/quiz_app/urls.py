from django.urls import path
from .views import WelcomeView, render_quiz, show_results

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('1/', render_quiz, name="render-quiz"),
    path('1/results/', show_results, name='show-results'),
              ]
