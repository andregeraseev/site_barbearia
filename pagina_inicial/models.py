from django.db import models

class Banner(models.Model):
    titulo = models.CharField(max_length= 100)
    texto = models.TextField()
    foto_banner = models.ImageField(upload_to='static/banners', blank= True)
    publicada = models.BooleanField(default=False)
    def __str__(self):
        return self.titulo

class Body(models.Model):
    titulo_body = models.CharField(max_length= 100)
    subtitulo_body = models.CharField(max_length= 200)
    texto_body = models.TextField()

    def __str__(self):
        return self.titulo_body

class FotosBody(models.Model):
    titulo_foto_body = models.CharField(max_length= 100)
    foto_body = models.ImageField(upload_to='static/foto_body', blank=True)

    def __str__(self):
        return self.titulo_foto_body
