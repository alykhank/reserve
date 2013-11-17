from django.contrib import admin
from claim.models import Resource, Game

class ResourceAdmin(admin.ModelAdmin):
	list_display = ('name', 'available', 'reservationTime')
	search_fields = ['name']

admin.site.register(Resource, ResourceAdmin)
admin.site.register(Game)
