from django.db import models

class Banner(models.Model):
    titulo = models.CharField(max_length= 100)
    texto = models.TextField()
    foto_banner = models.ImageField(upload_to='static/banners', blank= True)
    publicada = models.BooleanField(default=False)
    def __str__(self):
        return self.titulo
