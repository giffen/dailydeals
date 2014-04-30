import datetime
from django.db import models
from django.core.urlresolvers import reverse

class DealManager(models.Manager):
	def get_featured_deals(self):
		#return super(DealManager, self).filter(featured=True).filter(expire_date__gt=datetime.datetime)
		return super(DealManager, self).\
		filter(featured=True)

class Deal(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField()
	description = models.CharField(max_length=5000, blank=True, null=True)
	publication_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	expire_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
	remaining = models.IntegerField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=300, null=True, blank=True) 
	deal_price = models.DecimalField(decimal_places=2, max_digits=300, null=True, blank=True)
	featured = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	objects = DealManager()

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		year = self.publication_date.strftime("%Y")
		month = self.publication_date.strftime("%m")
		slug = self.slug
		return reverse('deal_detail', args=[year, month, slug])
		'''
		return "deals/%s/%s/%s/" %(self.publication_date.strftime("%Y"), 
															self.publication_date.strftime("%m"), 
															self.slug)
		'''