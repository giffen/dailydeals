from django.contrib import admin

from .forms import DealForm
from .models import Deal

class DealAdmin(admin.ModelAdmin):
	form = DealForm
	#class Meta:
	#	model = Deal

admin.site.register(Deal, DealAdmin)
