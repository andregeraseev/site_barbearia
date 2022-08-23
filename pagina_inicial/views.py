from django.shortcuts import render
from pagina_inicial.models import Banner, Body, FotosBody, AgendeBody, ContatoBody

def home(request):
    banner = Banner.objects.all()
    body = Body.objects.all()
    fotos_body = FotosBody.objects.all()
    agende_body = AgendeBody.objects.all()
    contato_body = ContatoBody.objects.all()

    dados = {'banners': banner, 'body': body, 'fotos': fotos_body, 'agende': agende_body,
             'contatos': contato_body}

    return render(request, 'pagina_inicial.html', dados)









