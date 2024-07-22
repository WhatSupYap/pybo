from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        # 아래 form.is_valid() 판단 기준은 어떻게 판단하는가?
        if form.is_valid(): # 폼이 유효하다면
            question = form.save(commit=False) # commit=False : 데이터베이스에 저장하지 않고 모델 객체만 가져옴 # 임시 저장하여 question 객체를 리턴받는다.
            question.author = request.user
            question.create_date = timezone.now() # 실제 저장을 위해 작성일시를 설정한다.
            question.save() # 데이터를 실제로 저장한다.
            return redirect('pybo:index')
    else:
        form = QuestionForm() # from .forms 이용 하여 가져옴
    context = {'form': form}
    return render(request, 'pybo/question_form.html', {'form': form})


@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # 수정할 질문을 가져온다.
    if request.user != question.author: # 작성자와 로그인한 사용자가 다를 경우
        messages.error(request, '수정권한이 없습니다') # messages.error() : 오류 메시지를 화면에 출력
        return redirect('pybo:detail', question_id=question.id) # 질문 상세 화면으로 이동
    if request.method == "POST": # POST 요청일 경우
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else: # GET 요청일 경우
        form = QuestionForm(instance=question) # 질문 수정 화면을 보여줄 때 기존 질문 데이터를 폼에 채워서 보여준다.
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')

@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)