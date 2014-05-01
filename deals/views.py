from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, Http404

from .models import Deal

def all_deals(request):
	all_posts = Deal.objects.all()
	paginator = Paginator(all_posts, 24) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)

	return render(request, 'deals/all.html', locals())


def year_archive(request, year):
	all_posts = Deal.objects.all().filter(publication_date__year=year)
	paginator = Paginator(all_posts, 24) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)

	if all_posts.count() == 0:
		raise Http404
		
	return render(request, 'deals/all.html', locals())


def month_archive(request, year, month):
	posts = Deal.objects.all().filter(publication_date__year=year).\
															filter(publication_date__month=month)

	if posts.count() == 0:
		raise Http404

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
