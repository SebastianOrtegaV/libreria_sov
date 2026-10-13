

from django.contrib import admin
from libreria.models import Editorial, Libro


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('editorial', 'nombre', 'precio_clp', 'disponible')
    list_filter = ('nombre', 'editorial')
    search_fields = ('nombre',)

    def precio_clp(self, obj):
        return f"${obj.precio:,}".replace(",", ".")

    precio_clp.short_description = 'Precio'
