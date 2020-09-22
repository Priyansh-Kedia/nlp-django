from django.urls import path

from .views import question_response

urlpatterns = [
    path('', question_response, name='question_response'),
]