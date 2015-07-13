from django.forms import ModelForm
from links.models import Link

class LinkForm(ModelForm):

	class Meta:
		model = Link
		fields = ['title', 'url'] 