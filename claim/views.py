from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages

from claim.models import Resource

class IndexView(generic.ListView):
	model = Resource
	template_name = 'claim/index.html'

class DetailView(generic.DetailView):
	model = Resource
	template_name = 'claim/detail.html'

def claim(request, pk):
	resource = get_object_or_404(Resource, pk=pk)
	if resource.available:
		resource.available = False
		resource.reservationTime = datetime.now()
		resource.save()
	else:
		messages.error(request, 'Resource is unavailable.')
	return HttpResponseRedirect(reverse('claim:index'))

def release(request, pk):
	resource = get_object_or_404(Resource, pk=pk)
	if not resource.available:
		resource.available = True
		resource.save()
	else:
		messages.error(request, 'Resource is available.')
	return HttpResponseRedirect(reverse('claim:index'))
