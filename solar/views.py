from solar.models import Predios

from django.shortcuts import render_to_response

def index(request):
	info = Predios.objects.all()
	return render_to_response('index.html',{'lista':info})

def nosotros(request):
	info = Predios.objects.all()
	return render_to_response('nosotros.html',{'lista':info})
def mas(request):
	info = Predios.objects.all()
	return render_to_response('mas.html',{'lista':info})
def laenergiasolar(request):
	info = Predios.objects.all()
	return render_to_response('laenergiasolar.html',{'lista':info})
def limitaciones(request):
	info = Predios.objects.all()
	return render_to_response('limitaciones.html',{'lista':info})