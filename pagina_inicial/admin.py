from django.contrib import admin
from .models import Banner, Body, FotosBody, AgendeBody, ContatoBody


class ListandoBanners(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'texto', 'foto_banner', 'publicada','banner_preview')
    list_display_links = ('id', 'titulo',)
    list_editable = ('publicada',)
    readonly_fields = ('banner_preview',)

    def banner_preview(self, obj):
        return obj.banner_preview

    banner_preview.short_description = 'banner preview'
    banner_preview.allow_tags = True


admin.site.register(Banner, ListandoBanners)

class ListandoBody(admin.ModelAdmin):
    list_display = ('id','titulo_body', 'texto_body')
    list_display_links = ('id','titulo_body')
    list_per_page = 10


admin.site.register(Body, ListandoBody)

class ListandoFotosBody(admin.ModelAdmin):
    list_display = ('id','titulo_foto_body', 'publicada_body', 'body_preview')
    list_display_links = ('id', 'titulo_foto_body')
    list_editable = ('publicada_body',)
    readonly_fields = ('body_preview',)
    list_per_page = 10

    def body_preview(self, obj):
        return obj.body_preview

    body_preview.short_description = 'body preview'
    body_preview.allow_tags = True


admin.site.register(FotosBody, ListandoFotosBody)

class ListandoAgendeBody(admin.ModelAdmin):
    list_display = ('id','titulo_agende','link_agende')
    list_display_links = ('id', 'titulo_agende')
    list_editable = ('link_agende',)
    list_per_page = 10

admin.site.register(AgendeBody, ListandoAgendeBody)

class ListandoContatoBody(admin.ModelAdmin):
    list_display = ('id','titulo_contato','subtitulo_contato', 'telefone_contato', 'email_contato')
    list_display_links = ('id', 'titulo_contato')
    list_editable = ('telefone_contato', 'email_contato',)
    list_per_page = 10

admin.site.register(ContatoBody, ListandoContatoBody)