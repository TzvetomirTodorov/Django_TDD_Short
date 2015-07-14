from urllib.parse import urlparse
from django.contrib import admin
from links.models import Link

class LinkAdmin(admin.ModelAdmin):
	list_display = ('title', 'link', 'submitted', 'score', 'submitted_by', 'booster_list',)
	search_fields = ('title', 'url', 'submitted_by__username',)
	readonly_fields = ('submitted_by', 'score', 'boosters',)
	# actions = ['add_submitter_to_boosters']

	def booster_list(self, link):
		return ", ".join([b.username for b in link.boosters.all()])
		booster_list.short_description = 'boosters'

	def link(self, link):
		return '<a href="{url}" target="blank">{text}</a>'.format(
			url=link.url, text=urlparse(link.url).netloc)
		link.allow_tags = True

	def save_model(self, request, obj, form, change):
		if not change:
			obj.submitted_by = request.user
		obj.save()

	def save_related(self, request, form, formsets, change):
		super(LinkAdmin, self).save_related(request, form, formsets, change)
		form.instance.boosters.add(form.instance.submitted_by)
		form.instance.score = 1


	# def add_submitter_to_boosters(modeladmin, request, queryset):
	# 	for link in queryset:
	# 		link.boosters.add(link.submitted_by)
	# 		link.score = link.boosters.all().count()
	# 		link.save()
	# add_submitter_to_boosters.short_description = "Add submitter to boosters"

admin.site.register(Link, LinkAdmin)
# Register your models here.
