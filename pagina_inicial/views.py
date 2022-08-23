from django.shortcuts import render
from pagina_inicial.models import Banner, Body, FotosBody

def home(request):
    banner = Banner.objects.all()
    body = Body.objects.all()
    fotos_body = FotosBody.objects.all()

    dados = {'banners': banner, 'body': body, 'fotos': fotos_body}

    return render(request, 'pagina_inicial.html', dados)









