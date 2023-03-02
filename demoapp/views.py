from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pytube import YouTube
import os
import requests
from pytube import streams
from demoapp.models import Blog



def how(request):
    post=Blog.objects.all()
    return render(request,'how.html',{'post':post})

def one(request):
    return render(request,"index.html")

def save(request):
    global url
    url=request.GET.get('url')
    obj=YouTube(url)
    Title=obj.title 
    Thamb=obj.thumbnail_url
    resolutions = obj.streams.filter( file_extension='mp4').order_by('resolution').desc().all()
    #resolutions=obj.streams.filter(progressive=True,file_extension='mp4').all()
    return render(request, 'download.html',{'rsl':resolutions, 'titl': Title , 'ytimg':Thamb})
from django.http import FileResponse

from django.http import StreamingHttpResponse

from django.shortcuts import render
from pytube import YouTube
import os

from django.shortcuts import render
from pytube import YouTube
import os
import json

def downloaded(request, resolution):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    video = YouTube(url)
    stream = video.streams.get_by_resolution(resolution)
    if stream is None:
        return render(request, 'fail.html')
    return render(request, 'popup.html', {'stream_json': json.dumps({'url': stream.url, 'title': stream.title})})

def come(request):
    return render(request,'coming.html')

def feed(request):
    return render(request,'feedback.html')

def pramote(request):
    return render(request,'promot.html')