# Create your views here.

from django.shortcuts import render, redirect

from quizzes.models import Quiz, Question, Answer

def example(request):
    td = {}
    
    quiz = Quiz.objects.get(pk = 1)
    questions = Question.objects.filter(quiz = quiz)
    question = questions[0]
    answers = Answer.objects.filter(question = question)
    
    td['question'] = question
    td['answers'] = answers
    
    return render(request, "quiz.html", td)

def get_out(request):
    return redirect("main.views.home")