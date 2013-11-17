from django.contrib import admin
from claim.models import Resource

class ResourceAdmin(admin.ModelAdmin):
	list_display = ('name', 'available', 'reservationTime')
	search_fields = ['name']

admin.site.register(Resource, ResourceAdmin)
