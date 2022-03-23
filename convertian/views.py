#file the i have created
from typing import ParamSpec
import pyrebase
from django.http import HttpResponse
from django.shortcuts import render
config={
    'apiKey': "AIzaSyDmEH8jXNgKHkglaglV7KRjM0o7MRasabs",
    'authDomain': "convert-fbfde.firebaseapp.com",
    'projectId': "convert-fbfde",
    'storageBucket': "convert-fbfde.appspot.com",
    'messagingSenderId': "238785399466",
    'appId': "1:238785399466:web:aff38fb167e404c1995ed3",
    'measurementId': "G-56EPEXLQLW",
    'databaseURL': ""
}
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
def signin(request):
     return render(request,'signin.html')
def postsign(request):
     email=request.POST.get('email')
     passw=request.POST.get('password')
     user=auth.sign_in_with_email_and_password(email,passw)
     params={'e':email}
     return render(request,'welcome.html',params)
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