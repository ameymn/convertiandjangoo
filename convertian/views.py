#file the i have created
from typing import ParamSpec
import pyrebase
import img2pdf
from PIL import Image 
import os
import fitz
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage, default_storage
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
    return redirect("http://127.0.0.1:8000/")
#def upload(request):
 #   if request.method == 'POST' and request.FILES['upload']:
  #      upload = request.FILES['upload']
   #     fss = FileSystemStorage()
    #    file = fss.save(upload.name, upload)
     #   file_url = fss.url(file)
      #  return render(request, 'imagetopdfsuccess.html')

def imagetopdf(request):
     if request.method=="POST":
          img=request.FILES['upload']
          print(img.name)
          print(img.size)
          file_name = default_storage.save(img.name, img)
          #file = default_storage.open(file_name)
          file_url = default_storage.url(file_name)
          pdf=fitz.open(file_url)
          page=pdf.loadPage(0)
          pix=page.getPixmap()
          pix.writeImage('')
          #n_fileurl=file_url.replace("/","\\")
          #print(file_url)
          #image = Image.open(r"C:\Users\91738\Desktop\Screenshot 2022-03-01 141707.png")
          #image.save(r'C:\Users\91738\Desktop\convertionj\convertian\results\rees.pdf')
          #pdf_bytes = img2pdf.convert(image.filename)
          #file = open(r"C:\Users\91738\Desktop\convertionj\convertian\results\res.pdf", "wb")
          #file.write(pdf_bytes)
          img.close()    
          #file.close()
  
     return render(request,'imagetopdf.html')

def pdftodoc(request):
     return render(request,'pdftodoc.html')

def imagetopdfsuccess(request):
     return render(request,'imagetopdf/imagetopdfsuccess.html')

def doctopdf(request):
     return render(request,'doctopdf.html')
def home(request):
     return render(request,'index.html')

def compressimage(request):
     return render(request,'compressimage.html')