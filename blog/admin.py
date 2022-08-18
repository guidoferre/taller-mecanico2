from django.contrib import admin

from blog.models import Avatar, cliente, mecanico, reparacion


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'vehiculo']
    search_fields = ['nombre']
# Register your models here.
admin.site.register(cliente, ClienteAdmin)
admin.site.register(mecanico)
admin.site.register(reparacion)
admin.site.register(Avatar)