from django.contrib import admin
from .models import UserStripe

class UserStripeAdmin(admin.ModelAdmin):
	class Meta:
		model = UserStripe

admin.site.register(UserStripe, UserStripeAdmin)
