from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Question, Choice
from django.views import generic

# Create your views here.
### Generic View (class-based views)
class IndexView(generic.ListView):
    template_name = 'midterm/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'midterm/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'midterm/results.html'

# def index(request):
#     # return HttpResponse("Hello, world. You're at the midterm index.")
#     latest_question_list=Question.objects.order_by('-pub_date')[:5]
#     # output=', '.join(q.question_text for q in latest_question_list)
#     # return HttpResponse(output)
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'midterm/index.html', context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'midterm/detail.html', {'question':question})

# def results(request, question_id):
#     # response=HttpResponse("You're looking ate the results of question %s." % question_id)
#     # return response
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'midterm/results.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form
        return render(request, 'midterm/detail.html', {
            'question':question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('midterm:results', args=(question_id,)))