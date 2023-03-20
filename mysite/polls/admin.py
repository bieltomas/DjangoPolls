from django.contrib import admin

from .models import Pregunta, Eleccion

class Opciones(admin.TabularInline):
    model = Eleccion
    extra = 1
class PreguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['textoPregunta']}),
        ('Date information', {'fields': ['fechaPublicacion']}),
    ]
    inlines = [Opciones]
    list_display = ('textoPregunta', 'fechaPublicacion', 'reciente')
    list_filter = ['fechaPublicacion']
    search_fields = ['textoPregunta']

admin.site.register(Pregunta, PreguntaAdmin)


