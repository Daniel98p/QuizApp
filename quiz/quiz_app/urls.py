from django.urls import path
from .views import WelcomeView, Index

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('1/', Index.as_view(), name="index"),
              ]
