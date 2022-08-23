from django.contrib import admin
from .models import Banner, Body, FotosBody


class ListandoBanners(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'texto', 'foto_banner', 'publicada')
    list_display_links = ('id', 'titulo')
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Banner, ListandoBanners)

class ListandoBody(admin.ModelAdmin):
    list_display = ('id','titulo_body', 'texto_body')
    list_display_links = ('id','titulo_body')
    list_per_page = 10


admin.site.register(Body, ListandoBody)

class ListandoFotosBody(admin.ModelAdmin):
    list_display = ('id','titulo_foto_body')
    list_display_links = ('id', 'titulo_foto_body')
    list_per_page = 10


admin.site.register(FotosBody, ListandoFotosBody)