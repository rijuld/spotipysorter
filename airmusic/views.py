
from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .models import method,list,color
from django.db.models import Max
import random
from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
	
cid = 'f77aede2e20d44129f4adb0381f6053c'
secret = '2dcac83437344bba93c9532aaf2271f8'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#https://open.spotify.com/user/31ftyjw6e552efnanwvepgiyis6i?si=be7affcc1ca145f6
def index(request):
	#TODO do something here
	a=1
	return render(request, "airmusic/index.html",{'a': a})

##################################################################################################################################
def get_random3():
		max_id = method.objects.all().aggregate(max_id=Max("id"))['max_id']
		while True:
			pk = random.randint(1, max_id)
			if pk:
				return pk
##################################################################################################################################

def page1(request):
	#TODO do something here
	try:    
		id = int(request.GET.get('id'))
	except Exception as e:
		id = get_random3()
	print("blah blah blah" + str(id))
	item=method.objects.get(pk=id)
	orgs = list.objects.filter(post=item)
	flag=1
	if not orgs:
		flag=0
	return render(request, "airmusic/page1.html",{'item':item,'flag':flag})

##################################################################################################################################
##################################################################################################################################

def page2(request):
	#TODO do something here
	queryset=list.objects.all()
	a=queryset[0]
	return render(request, "airmusic/page2.html",{'a': a,'queryset':queryset})

##################################################################################################################################
##################################################################################################################################

def page3(request):
	#TODO do something here
	a=1

	return render(request, "airmusic/page3.html",{'a': a})
	

##################################################################################################################################
##################################################################################################################################

def searchresult(request):   
	query = request.GET.get('q')
	#TODO do something here
	queryset=method.objects.filter(function__icontains=query)
	a=1
	return render(request, "airmusic/searchresult.html",{"queryset": queryset})

##################################################################################################################################
##################################################################################################################################
@csrf_exempt
def page1add(request):
	if request.method !="POST": return JsonResponse({"error":"POST request required"},status=400)
	data = json.loads(request.body)
	id = data.get("id", "")
	post=method.objects.get(id=id)
	k=list(post=post)
	k.save()
	#ToDo something here
	return JsonResponse({"message":"Your item has been added"},status=201)

##################################################################################################################################
##################################################################################################################################
@csrf_exempt
def page1remove(request):
	if request.method !="POST": return JsonResponse({"error":"POST request required"},status=400)
	data = json.loads(request.body)
	id = data.get("id", "")
	post=method.objects.get(id=id)
	k=list.objects.get(post=post)
	k.delete()
	return JsonResponse({"message":"Your item has been removed"},status=201)

##################################################################################################################################
##################################################################################################################################
@csrf_exempt
def page1textarea(request):
	if request.method !="POST": return JsonResponse({"error":"POST request required"},status=400)
	data = json.loads(request.body)
	id = data.get("id", "")
	text = data.get("text", "")
	post=method.objects.get(id=id)
	post.json=text
	post.save()
	return JsonResponse({"message":"Your text has been edited!"},status=201)

##################################################################################################################################
##################################################################################################################################

def all(request):   
	queryset=method.objects.all()
	return render(request, "airmusic/all.html",{'queryset': queryset})
	
def colors(request):   
	queryset=method.objects.all()
	return render(request, "airmusic/colors.html")