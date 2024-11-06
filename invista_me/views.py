from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoForm
# Create your views here.


def investimento(request):
    dados = {
        "dados":Investimento.objects.all()
    }
    return render(request, "investimentos/investimento.html", context=dados)

def detalhe(request, id_investimento):
    dados= {
        "dados" : Investimento.objects.get(pk=id_investimento)
    }
    return render(request, 'investimentos/detalhe.html',dados)

def criar(request):
    if request.method == "POST":
        investimento_form = InvestimentoForm (request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect("investimento")
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            "formulario": investimento_form
    }
    return render(request, "investimentos/novo_investimento.html/", context=formulario)

def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    
    #novo_investimento/1 -> GET
    if request.method == "GET":
        formulario = InvestimentoForm(instance=investimento)
        return render(request,"investimentos/novo_investimento.html", {"formulario": formulario})

    #caso a requisição seja POST
    else:
        formulario = InvestimentoForm(request.POST,instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect("investimento")
    
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == "POST":
        investimento.delete()
        return redirect("investimento")
    return render(request, "investimentos/confirmar_exclusao.html",{'item': investimento})