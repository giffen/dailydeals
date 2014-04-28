from django.db import models
from django.contrib.auth.models import User

class UserStripe(models.Model):
	user = models.OneToOneField(User)
	stripe_id = models.CharField(max_length=120, null=True, blank=True)
	phone_number = models.CharField(max_length=120, default='555-555-5555')

	def __unicode__(self):
		return self.user.username


