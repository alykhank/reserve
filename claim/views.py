from django.shortcuts import render, get_object_or_404
from django.views import generic

from claim.models import Resource

class IndexView(generic.ListView):
	model = Resource
	template_name = 'claim/index.html'
