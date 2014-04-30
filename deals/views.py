from django.shortcuts import render, Http404

from .models import Deal

def deal_detail(request, year, month, slug):

	try:
		post = Deal.objects.filter(publication_date__year=year).\
															filter(publication_date__month=month).\
															get(slug=slug)
	except Deal.MultipleObjectsReturned:
		post = Deal.objects.filter(publication_date__year=year).\
															filter(publication_date__month=month).\
															filter(slug=slug)[0]
	except:
		raise Http404

	context = {
		'year' : year,
		'month' : month,
		'slug' : slug,
		'post' : post
	}

	return render(request, 'deals/deal_detail.html', context)
