from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

from django.shortcuts import render
from .models import Question


def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)