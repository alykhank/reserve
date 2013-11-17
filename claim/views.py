from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from claim.models import Resource, Game

class ResourceCreate(generic.edit.CreateView):
	model = Resource
	fields = '__all__'
	success_url = 'claim:index'

class IndexView(generic.ListView):
	model = Resource
	template_name = 'claim/index.html'

class DetailView(generic.DetailView):
	model = Resource
	template_name = 'claim/detail.html'

def claim(request, pk):
	resource = get_object_or_404(Resource, pk=pk)
	userEmail = request.POST.get('userEmailAddress')
	friendEmail = request.POST.get('friendEmailAddress')
	if resource.available:
		resource.available = False
		resource.reservationTime = timezone.now()
		resource.save()
		game = Game(resource=resource, player1=userEmail, player2=friendEmail, homeScore=0, awayScore=0)
		game.save()
		send_mail('[Reserve] ' + resource.name + ' Claimed', 'A match between ' + userEmail + ' and ' + friendEmail + ' will now commence.', settings.SERVER_EMAIL, [userEmail, friendEmail], fail_silently=False)
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

def goal(request, resource_id, game_id, player):
	game = get_object_or_404(Game, pk=game_id)
	if player == '1':
		game.homeScore += 1
	elif player == '2':
		game.awayScore += 1
	game.save()
	return HttpResponseRedirect(reverse('claim:detail', kwargs={'pk': resource_id}))
