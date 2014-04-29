from django.db import models

class Contact(models.Model):
	email = models.EmailField()
	message = models.CharField(max_length=4000)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self, ):
		return str(self.email)

