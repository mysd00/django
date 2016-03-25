from django.template import loader
from django.http import Http404
from .models import Choice, Question, Q_number
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    #In the future instead of 20 it should be possible to change it from admin
    latest_question_list = Question.objects.order_by('-pub_date')[:20]
    template = loader.get_template('polls/index.html')
    # it is possible to set choices in this way
    ch1 = Choice(choice_text = 'you can find me in views.py',question_id=1)
    ch1.save()
    #Context is a dictionary mapping template variable names to Python objects. It is neccessary for passing var to index
    context = {
        'latest_question_list': latest_question_list,
    }
    # isntead render() method can be used
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
