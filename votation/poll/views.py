from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Questions

# Create your views here.
# o index é comumente a nomeação da página inicial


def index(request):
    # return HttpResponse('Olá mundo!')
    latest_question_list = Questions.objects.order_by('-pub_date')[:5] # Ordena as últimas 5 perguntas com base na data de publicação;
    context = {'latest_question_list': latest_question_list} # monta a variavel em objeto para como vai aparecer lá na página;
    return render(request, 'poll/index.html', context) # 'render' => 'renderiza' a página pra mim baseada em uma request na página poll/index.html (que será criada) e mostra o valor 'context'.


""" def detail(request, question_id):
    return HttpResponse('Essa é a pergunta de número %s' %question_id) """

def results(request, question_id):
    # return HttpResponse('Esses são os resultados da pergunta de número %s' %question_id)
    question = Questions(pk=question_id) # pk = primary key
    return render(request, 'poll/results.html', {'question': question})

def vote(request, question_id):
    # return HttpResponse('Você está votando na questão de número %s' %question_id)
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return render(request, 'poll/vote.html',{
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        print('laura')
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))