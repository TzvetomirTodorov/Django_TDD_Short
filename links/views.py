from django.shortcuts import render
from links.models import Link

def home(request):
	links = Link.objects.all().order_by('-submitted')[:15]
	return render(request, 'home.html', {'links':links})
