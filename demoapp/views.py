from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect,requires_csrf_token,ensure_csrf_cookie
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
from django.http import FileResponse

from django.http import StreamingHttpResponse

from django.shortcuts import render
from pytube import YouTube
import os

from django.shortcuts import render
from pytube import YouTube
import os
import json


def come(request):
    return render(request,'coming.html')

def feed(request):
    return render(request,'feedback.html')

def pramote(request):
    return render(request,'promot.html')

# just leave it
from django.views.decorators.csrf import csrf_protect
@csrf_exempt
@csrf_protect
def save(request):
    global url
    url = request.GET.get('url')
    if not url:
        return render(request, 'download.html', {'alert': 'Please enter a valid YouTube video URL.'})
    try:
        obj = YouTube(url)
    except:
        return render(request, 'download.html', {'alert': 'Video is not available. Please try a different URL.'})
    Title = obj.title 
    Thamb = obj.thumbnail_url
    resolutions = [stream for stream in obj.streams.filter(file_extension='mp4',progressive=True).order_by('resolution').desc() if stream]
    audio_streams = [stream for stream in obj.streams.filter(file_extension='mp4', type='audio') if stream]

    # Store the URL in the user's session
    request.session['url'] = url

    return render(request, 'download.html', {'rsl': resolutions,'sang':audio_streams,'titl': Title, 'ytimg': Thamb})

from pytube.exceptions import PytubeError
from django.views.decorators.csrf import csrf_protect
@csrf_exempt
@csrf_protect
def downloaded(request, resolution):
    global url
    if not url:
        return render(request, 'fail.html', {'tappu': 'Please refresh and try again! Thanks for visiting.'})

    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    try:
        video = YouTube(url)
        stream = video.streams.get_by_resolution(resolution)
        if stream is None:
            return render(request, 'fail.html')
        return render(request, 'popup.html', {'stream_json': json.dumps({'url': stream.url, 'title': stream.title})})
    except PytubeError:
        return render(request, 'fail.html', {'tappu': 'please go back and try again later.'})
from django.views.decorators.csrf import csrf_protect
@csrf_exempt
@csrf_protect
def song(request, abr):
    global url
    if not url:
        return render(request, 'fail.html',{'tappu':'please refresh and try again! thanks for visit,thanks'})
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    try:
        video = YouTube(url)
        strea = video.streams.get_audio_only()
        if strea is None:
            return render(request, 'fail.html')
        return render(request, 'popup.html', {'stream_json': json.dumps({'url': strea.url, 'title': strea.title})})
    except:
        return render(request, 'fail.html',{'tappu':'please refresh and try again! thanks for visit'})
