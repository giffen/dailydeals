from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		widgets = { 'message': forms.Textarea(attrs={'cols':80,'rows':20}), }