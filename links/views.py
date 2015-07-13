from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from links.models import Link
from links.forms import LinkForm

def home(request):
	links = Link.objects.all().order_by('-submitted')[:15]
	return render(request, 'home.html', {'links':links})

@login_required()
def new_link(request):
	if request.method == 'POST':
		form = LinkForm(request.POST)
		if form.is_valid():
			link = form.save(commit = False)
			link.submitted_by = request.user
			link.save()
			
		return HttpResponseRedirect('/')
	else:
		form = LinkForm()
	
	return render(request, 'new_link.html', {'form': form})
