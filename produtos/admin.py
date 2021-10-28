from django.contrib import admin

from .models import Arquivo, Item, Produto

admin.site.register(Produto)
admin.site.register(Item)
admin.site.register(Arquivo)