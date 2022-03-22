#file the i have created
from typing import ParamSpec
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    params={'name':'amey','place':'earth'}
    return render(request,'index.html',params)

def imagetopdf(request):
     return render(request,'imagetopdf.html')

def pdftodoc(request):
     return render(request,'pdftodoc.html')

def doctopdf(request):
     return render(request,'doctopdf.html')


def compressimage(request):
     return render(request,'compressimage.html')