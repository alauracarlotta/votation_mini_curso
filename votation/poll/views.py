from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# o index é comumente a nomeação da página inicial
def index(request):
    return HttpResponse('Olá mundo!')
