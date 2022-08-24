from django.shortcuts import render
from pagina_inicial.models import Banner, Body, FotosBody, AgendeBody, ContatoBody
from django_filters import filters


def home(request):
    banner = Banner.objects.all()
    body = Body.objects.all()
    fotos_body = FotosBody.objects.all()
    agende_body = AgendeBody.objects.all()
    contato_body = ContatoBody.objects.all()


    dados = {'banners': banner, 'body': body, 'fotos': fotos_body, 'agende': agende_body,
             'contatos': contato_body}

    return render(request, 'pagina_inicial.html', dados)

def teste(request):
    fotos_body = FotosBody.objects.all()

    dados = {'fotos': fotos_body}

    return render(request, 'carrocel.html', dados)







