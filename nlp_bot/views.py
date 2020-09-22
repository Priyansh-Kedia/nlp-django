from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Question
from . import response_generator

@csrf_exempt
@api_view(['POST',])
def question_response(request):
    question = request.POST.get('question')
    questions = Question.objects.all()
    questions_list = [question.question_text for question in questions]
    response = response_generator.getMaxSimilarity(question, questions)
    return Response({'message':response.answer_text})

