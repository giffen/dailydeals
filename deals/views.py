from django.shortcuts import render, Http404

from .models import Deal

def deal_detail(request, year, month, slug):

	return render(request, 'deals/deal_detail.html', locals())
