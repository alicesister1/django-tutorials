# Create your views here.
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        pub_date 가 현재보다 작거나 같은 질문 중 최근 5개만 반환한다.
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        아직 게재 시점이 아닌 질문은 제외한다.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        """
        아직 게재 시점이 아닌 질문은 제외한다.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # details 투표 폼을 다시 표시
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        # https://docs.djangoproject.com/ko/3.1/ref/models/expressions/#f-expressions
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # 뒤로가기 눌렀을 때 같은 폼이 두번 제출되는 경우 방지를 위해
        # POST가 성공적으로 끝난 후 항상 HttpResponseRedirect를 반환
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
