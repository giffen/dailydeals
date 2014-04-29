from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from django.core.mail import send_mail

from .models import Contact
from .forms import ContactForm

def contact(request):

	form = ContactForm(request.POST or None)

	if form.is_valid():
		save_form = form.save(commit=False)
		save_form.save()

	return render_to_response('form.html', locals(), context_instance=RequestContext(request))
