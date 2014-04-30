from django.shortcuts import render, Http404

from .models import Deal

def all_deals(request):
	posts = Deal.objects.filter(featured=True)
	return render(request, 'deals/all.html', locals())


def year_archive(request, year):
	posts = Deal.objects.filter(publication_date__year=year)

	return render(request, 'deals/all.html', locals())


def month_archive(request, year, month):
	posts = Deal.objects.filter(publication_date__year=year).\
															filter(publication_date__month=month)

	return render(request, 'deals/all.html', locals())


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
