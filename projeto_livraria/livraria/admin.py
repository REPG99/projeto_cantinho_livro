from django.contrib import admin
from .models import Livro

class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'estoque', 'autor')
    list_filter = ('autor',)
    search_fields = ('nome', 'autor')

admin.site.register(Livro, LivroAdmin)