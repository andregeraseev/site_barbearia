from django.contrib import admin
from .models import Banner


class ListandoBanners(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'texto', 'foto_banner', 'publicada')
    list_display_links = ('id', 'titulo')
    search_fields = ('nome_receita',)
    list_editable = ('publicada',)
    list_per_page = 10


admin.site.register(Banner, ListandoBanners)
