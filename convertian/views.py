#file the i have created
import imp
from pickletools import optimize
from typing import ParamSpec
import pyrebase
import img2pdf
from PIL import Image
import aspose.words as aw 
import PIL
import os
import time
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
import comtypes.client
from docx2pdf import convert
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
storage=firebase.storage()
def signin(request):
     return render(request,'signin.html')
def signup(request):
     return render(request,'signup.html')
def postsign(request):
     email=request.POST.get('email')
     passw=request.POST.get('password')
     user=auth.sign_in_with_email_and_password(email,passw)
     params={'e':email}
     return render(request,'welcome.html',params)
def postsignup(request):
     email=request.POST.get('email')
     passw=request.POST.get('password')
     print(email)
     print(passw)
     user=auth.create_user_with_email_and_password(email,passw)
     return render(request,'welcome.html')
def index(request):
    return redirect("http://127.0.0.1:8000/")
#def upload(request):
 #   if request.method == 'POST' and request.FILES['upload']:
  #      upload = request.FILES['upload']
   #     fss = FileSystemStorage()
    #    file = fss.save(upload.name, upload)
     #   file_url = fss.url(file)
      #  return render(request, 'imagetopdfsuccess.html')

def currency(request):
     return render(request,'currency.html')
def currencyprocess(request):
     fromvalue=request.POST.get('from')
     fromunit=request.POST.get('currency')
     tounit=request.POST.get('currencyto')
     if tounit=='BTC':
          bitcoin=BtcConverter()
          toamount=bitcoin.convert_to_btc(float(fromvalue),fromunit)
     elif fromunit=='BTC':
          bitcoin=BtcConverter()
          toamount=bitcoin.convert_btc_to_cur(float(fromvalue),tounit)
     else:
          currency=CurrencyRates()
          val=currency.convert(fromunit,tounit,float(fromvalue))
          toamount=round(val,3)
     params={'fv':fromvalue,'fu':fromunit,'ta':toamount,'tu':tounit}
     return render(request,'currencyprocess.html',params)
     
def length(request):
     return render(request,'length.html')

def lengthprocess(request):
     fromvalue=request.POST.get('from')
     fromunit=request.POST.get('Length')
     tounit=request.POST.get('Lengthto')
     fromvalue=float(fromvalue)
     if tounit=='mm':
          if fromunit=='cm':
               tovalue=fromvalue*10
          elif fromunit=='m':
               tovalue=fromvalue*1000
          elif fromunit=='km':
               tovalue=fromvalue*1000000
          elif fromunit=='Mile':
               tovalue=fromvalue*1609334
          elif fromunit=='Yard':
               tovalue=fromvalue*914
          elif fromunit=='Foot':
               tovalue=fromvalue*305
          elif fromunit=='Inch':
               tovalue=fromvalue*25.4
          elif fromunit=='Light-year':
               tovalue=fromvalue*0.000000000000000009223
          elif fromunit=='mm':
               tovalue=fromvalue
     elif tounit=='cm':
          if fromunit=='mm':
                   tovalue=fromvalue/10
          elif fromunit=='m':
               tovalue=fromvalue*100
          elif fromunit=='km':
               tovalue=fromvalue*100000
          elif fromunit=='Mile':
               tovalue=fromvalue*160934
          elif fromunit=='Yard':
               tovalue=fromvalue*91.44
          elif fromunit=='Foot':
               tovalue=fromvalue*30.48
          elif fromunit=='Inch':
               tovalue=fromvalue*2.54
          elif fromunit=='Light-year':
               tovalue=fromvalue*946100000000000000
          elif fromunit=='cm':
               tovalue=fromvalue
     elif tounit=='m':
          if fromunit=='mm':
                   tovalue=fromvalue*0.001
          elif fromunit=='cm':
               tovalue=fromvalue*0.01
          elif fromunit=='km':
               tovalue=fromvalue*1000
          elif fromunit=='Mile':
               tovalue=fromvalue*1609.34
          elif fromunit=='Yard':
               tovalue=fromvalue*0.9144
          elif fromunit=='Foot':
               tovalue=fromvalue*0.3048
          elif fromunit=='Inch':
               tovalue=fromvalue*0.0254
          elif fromunit=='Light-year':
               tovalue=fromvalue* 9461000000000000.0
          elif fromunit=='m':
               tovalue=fromvalue
     elif tounit=='km':
          if fromunit=='mm':
                   tovalue=fromvalue*0.000001
          elif fromunit=='cm':
               tovalue=fromvalue*0.00001
          elif fromunit=='m':
               tovalue=fromvalue*0.001
          elif fromunit=='Mile':
               tovalue=fromvalue*1.60934
          elif fromunit=='Yard':
               tovalue=fromvalue*0.0009144
          elif fromunit=='Foot':
               tovalue=fromvalue*0.0003048
          elif fromunit=='Inch':
               tovalue=fromvalue*0.0000254
          elif fromunit=='Light-year':
               tovalue=fromvalue* 9461000000000000.0
          elif fromunit=='km':
               tovalue=fromvalue
     elif tounit=='Mile':
          if fromunit=='mm':
               tovalue=fromvalue*0.00000062317
          elif fromunit=='cm':
               tovalue=fromvalue*0.0000062317
          elif fromunit=='m':
               tovalue=fromvalue*0.000621371
          elif fromunit=='km':
               tovalue=fromvalue/1.609
          elif fromunit=='Yard':
               tovalue=fromvalue*0.000568182
          elif fromunit=='Foot':
               tovalue=fromvalue*0.000189394
          elif fromunit=='Inch':
               tovalue=fromvalue*0.000015783
          elif fromunit=='Light-year':
               tovalue=fromvalue*5879000000000.0
          elif fromunit=='Mile':
               tovalue=fromvalue
     elif tounit=='Yard':
          if fromunit=='mm':
               tovalue=fromvalue*0.00109361
          elif fromunit=='cm':
               tovalue=fromvalue*0.0109361
          elif fromunit=='m':
               tovalue=fromvalue*1.09361
          elif fromunit=='km':
               tovalue=fromvalue*1093.61
          elif fromunit=='Mile':
               tovalue=fromvalue*1760
          elif fromunit=='Foot':
               tovalue=fromvalue*0.333333
          elif fromunit=='Inch':
               tovalue=fromvalue*0.0277778
          elif fromunit=='Light-year':
               tovalue=fromvalue*10346388930000000.0
          elif fromunit=='Yard':
               tovalue=fromvalue
     elif tounit=='Foot':
          if fromunit=='mm':
               tovalue=fromvalue*0.00328084251969
          elif fromunit=='cm':
               tovalue=fromvalue*0.032808425196899998477
          elif fromunit=='m':
               tovalue=fromvalue*3.28084
          elif fromunit=='km':
               tovalue=fromvalue*3280.84
          elif fromunit=='Mile':
               tovalue=fromvalue*5280
          elif fromunit=='Yard':
               tovalue=fromvalue*3
          elif fromunit=='Inch':
               tovalue=fromvalue*0.0833333
          elif fromunit=='Light-year':
               tovalue=fromvalue*310400000000000000.0
          elif fromunit=='Foot':
               tovalue=fromvalue
     elif tounit=='Inch':
          if fromunit=='mm':
               tovalue=fromvalue*0.0393701
          elif fromunit=='cm':
               tovalue=fromvalue*0.393701
          elif fromunit=='m':
               tovalue=fromvalue*39.3701
          elif fromunit=='km':
               tovalue=fromvalue*39370.1
          elif fromunit=='Mile':
               tovalue=fromvalue* 63360
          elif fromunit=='Foot':
               tovalue=fromvalue*12
          elif fromunit=='Yard':
               tovalue=fromvalue*36
          elif fromunit=='Light-year':
               tovalue=fromvalue*372500000000000000.0
          elif fromunit=='Inch':
               tovalue=fromvalue
     elif tounit=='Light-year':
          if fromunit=='mm':
               tovalue=fromvalue*0.00000000000000000001057
          elif fromunit=='cm':
               tovalue=fromvalue*0.0000000000000000001057
          elif fromunit=='m':
               tovalue=fromvalue*0.0000000000000001057
          elif fromunit=='km':
               tovalue=fromvalue*0.0000000000001057
          elif fromunit=='Mile':
               tovalue=fromvalue*0.00000000000017011
          elif fromunit=='Foot':
               tovalue=fromvalue*0.000000000000000032217
          elif fromunit=='Yard':
               tovalue=fromvalue*0.000000000000000096652
          elif fromunit=='Inch':
               tovalue=fromvalue*0.0000000000000000026848
          elif fromunit=='Light-year':
               tovalue=fromvalue
     params={'fv':fromvalue,'fu':fromunit,'tv':tovalue,'tu':tounit}
     return render(request,'lengthsuccess.html',params)

def area(request):
     return render(request,'area.html')
def areaprocess(request):
     fromvalue=request.POST.get('from')
     fromunit=request.POST.get('area')
     tounit=request.POST.get('areato')
     tovalue=0
     fromvalue=float(fromvalue)
     if tounit=='mm²':
          if fromunit=='cm²':
               tovalue=fromvalue*100
          elif fromunit=='km²':
               tovalue=fromvalue*1000000000000
          elif fromunit=='acre':
               tovalue=fromvalue*4046856422
          elif fromunit=='Hectare':
               tovalue=fromvalue*10000000000
          elif fromunit=='mm²':
               tovalue=fromvalue
     elif tounit=='cm²':
          if fromunit=='mm²':
               tovalue=fromvalue/100
          elif fromunit=='km²':
               tovalue=fromvalue*10000000000.0
          elif fromunit=='acre':
               tovalue=fromvalue*4.047*10000000
          elif fromunit=='Hectare':
               tovalue=fromvalue*100000000
          elif fromunit=='cm²':
               tovalue=fromvalue
     elif tounit=='km²':
          if fromunit=='mm²':
               tovalue=fromvalue/1000000000000 
          elif fromunit=='cm²':
               tovalue=fromvalue/10000000000.0
          elif fromunit=='acre':
               tovalue=fromvalue/247
          elif fromunit=='Hectare':
               tovalue=fromvalue/100
          elif fromunit=='km²':
               tovalue=fromvalue
     elif tounit=='acre':
          if fromunit=='mm²':
               tovalue=fromvalue/4046856422
          elif fromunit=='cm²':
               tovalue=fromvalue/(4.047 * 10000000)
          elif fromunit=='km²':
               tovalue=fromvalue*247.105
          elif fromunit=='Hectare':
               tovalue=fromvalue*2.471
          elif fromunit=='acre':
               tovalue=fromvalue
     elif tounit=='Hectare':
          if fromunit=='mm²':
               tovalue=fromvalue/645
          elif fromunit=='cm²':
               tovalue=fromvalue/100000000
          elif fromunit=='km²':
               tovalue=fromvalue*100
          elif fromunit=='acre':
               tovalue=fromvalue/2.471
          elif fromunit=='Hectare':
               tovalue=fromvalue
     
     params={'fv':fromvalue,'fu':fromunit,'tv':tovalue,'tu':tounit}
     return render(request,'areaprocess.html',params)
def volume(request):
     return render(request,'volume.html')
def volumeprocess(request):
     fromvalue=request.POST.get('from')
     fromunit=request.POST.get('volume')
     tounit=request.POST.get('volumeto')
     tovalue=0
     fromvalue=float(fromvalue)
     if tounit=='mL':
          if fromunit=='L':
               tovalue=fromvalue*1000
          elif fromunit=='kL':
               tovalue=fromvalue*1000000
          elif fromunit=='gal':
               tovalue=fromvalue*3785.41
          elif fromunit=='cm³':
               tovalue=fromvalue
          elif fromunit=='m³':
               tovalue=fromvalue*1000000
          elif fromunit=='mL':
               tovalue=fromvalue
     elif tounit=='L':
          if fromunit=='mL':
               tovalue=fromvalue/1000
          elif fromunit=='kL':
               tovalue=fromvalue*1000
          elif fromunit=='gal':
               tovalue=fromvalue*3.78541
          elif fromunit=='cm³':
               tovalue=fromvalue/1000
          elif fromunit=='m³':
               tovalue=fromvalue*1000
          elif fromunit=='L':
               tovalue=fromvalue
     elif tounit=='kL':
          if fromunit=='mL':
               tovalue=fromvalue/1000000
          elif fromunit=='L':
               tovalue=fromvalue/1000
               print(tovalue)
          elif fromunit=='gal':
               tovalue=fromvalue/264.172
          elif fromunit=='cm³':
               tovalue=fromvalue/1000000
          elif fromunit=='m³':
               tovalue=fromvalue
          elif fromunit=='kL':
               tovalue=fromvalue
     elif tounit=='gal':
          if fromunit=='mL':
               tovalue=fromvalue/3785
          elif fromunit=='L':
               tovalue=fromvalue/3.78541
          elif fromunit=='kL':
               tovalue=fromvalue*264.172
          elif fromunit=='cm³':
               tovalue=fromvalue/3785
          elif fromunit=='m³':
               tovalue=fromvalue*264.172
          elif fromunit=='gal':
               tovalue=fromvalue
     elif tounit=='cm³':
          if fromunit=='mL':
               tovalue=fromvalue
          elif fromunit=='L':
               tovalue=fromvalue/1000
          elif fromunit=='kL':
               tovalue=fromvalue*1000
          elif fromunit=='gal':
               tovalue=fromvalue*3785.41
          elif fromunit=='m³':
               tovalue=fromvalue*1000000
          elif fromunit=='cm³':
               tovalue=fromvalue
     elif tounit=='m³':
          if fromunit=='mL':
               tovalue=fromvalue/1000000
          elif fromunit=='L':
               tovalue=fromvalue/1000
          elif fromunit=='kL':
               tovalue=fromvalue
          elif fromunit=='gal':
               tovalue=fromvalue/264.172
          elif fromunit=='cm³':
               tovalue=fromvalue/1000000
          elif fromunit=='m³':
               tovalue=fromvalue
     tovalue=float(tovalue)
     print(fromvalue,fromunit,tounit,tovalue)
     params={'fv':fromvalue,'fu':fromunit,'tv':tovalue,'tu':tounit}
     return render(request,'volumeprocess.html',params)
def temperature(request):
     return render(request,'temperature.html')
def temperatureprocess(request):
     fromvalue=request.POST.get('from')
     fromunit=request.POST.get('temperature')
     tounit=request.POST.get('temperatureto')
     fromvalue=float(fromvalue)
     if tounit=='Celsius':
          if fromunit=='Kelvin':
               tovalue=(fromvalue-273.15)
          elif fromunit=='Fahrenheit':
               tovalue=((fromvalue-32)*0.555)
          elif fromunit=='Celsius':
               tovalue=fromvalue
     if tounit=='Kelvin':
          if fromunit=='Celsius':
               tovalue=(fromvalue+273.15)
          elif fromunit=='Fahrenheit':
               tovalue=((fromvalue-32)*(5/9)+273.15)
          elif fromunit=='Kelvin':
               tovalue=fromvalue
     if tounit=='Fahrenheit':
          if fromunit=='Kelvin':
               tovalue=((fromvalue-273.15)*(1.8)+32)
          elif fromunit=='Celsius':
               tovalue=((fromvalue*1.8)+32)
          elif fromunit=='Fahrenheit':
               tovalue=fromvalue
          
     params={'fv':fromvalue,'fu':fromunit,'tv':tovalue,'tu':tounit}
     return render(request,'temperatureprocess.html',params )
def pressure(request):
     return render(request,'pressure.html')
def pressureprocess(request):
     fromvalue=request.POST.get('from')
     fromunit=request.POST.get('pressure')
     tounit=request.POST.get('pressureto')
     fromvalue=float(fromvalue)
     if tounit=='Psi':
          if fromunit=='Pa':
               tovalue=fromvalue/6895
          elif fromunit=='kPa':
               tovalue=fromvalue/6.895
          elif fromunit=='Barr':
               tovalue=fromvalue*14.504
          elif fromunit=='Atm':
               tovalue=fromvalue*14.696
          elif fromunit=='Torr':
               tovalue=fromvalue/51.715
          elif fromunit=='Psi':
               tovalue=fromvalue
     elif tounit=='Pa':
          if fromunit=='Psi':
               tovalue=fromvalue*6894.757
          elif fromunit=='kPa':
               tovalue=fromvalue*1000
          elif fromunit=='Barr':
               tovalue=fromvalue*100000.0
          elif fromunit=='Atm':
               tovalue=fromvalue*101325.0
          elif fromunit=='Torr':
               tovalue=fromvalue*133.322
          elif fromunit=='Pa':
               tovalue=fromvalue
     elif tounit=='kPa':
          if fromunit=='Psi':
               tovalue=fromvalue*6.895
          elif fromunit=='Pa':
               tovalue=fromvalue/ 1000.0
          elif fromunit=='Barr':
               tovalue=fromvalue*100.0
          elif fromunit=='Atm':
               tovalue=fromvalue*101.325
          elif fromunit=='Torr':
               tovalue=fromvalue/7.5062
          elif fromunit=='kPa':
               tovalue=fromvalue
     elif tounit=='Barr':
          if fromunit=='Psi':
               tovalue=fromvalue/14.504
          elif fromunit=='Pa':
               tovalue=fromvalue/100000.0
          elif fromunit=='kPa':
               tovalue=fromvalue/100.0
          elif fromunit=='Atm':
               tovalue=fromvalue*1.013
          elif fromunit=='Torr':
               tovalue=fromvalue/750.062
          elif fromunit=='Barr':
               tovalue=fromvalue
     elif tounit=='Atm':
          if fromunit=='Psi':
               tovalue=fromvalue/14.696
          elif fromunit=='Pa':
               tovalue=fromvalue/101325.0
          elif fromunit=='kPa':
               tovalue=fromvalue/101.0
          elif fromunit=='Barr':
               tovalue=fromvalue/1.013
          elif fromunit=='Torr':
               tovalue=fromvalue/750.062
          elif fromunit=='Atm':
               tovalue=fromvalue
     elif tounit=='Torr':
          if fromunit=='Psi':
               tovalue=fromvalue*51.715
          elif fromunit=='Pa':
               tovalue=fromvalue/133.0
          elif fromunit=='kPa':
               tovalue=fromvalue*7.501
          elif fromunit=='Atm':
               tovalue=fromvalue*760
          elif fromunit=='Barr':
               tovalue=fromvalue*750.062
          elif fromunit=='Torr':
               tovalue=fromvalue
     params={'fv':fromvalue,'fu':fromunit,'tv':tovalue,'tu':tounit}
     return render(request,'pressureprocess.html',params)
def numbersystem(request):
     return render(request,'numbersystem.html')
def numbersystemprocess(request):
     fromvalue=request.POST.get('from')
     fromunit=request.POST.get('numbersystem')
     tounit=request.POST.get('numbersystemto')
     tovalue=0
     if tounit=='BINARY':
          if fromunit=='HEXADECIMAL':
               tovalue=format(int(fromvalue,16),'b')
          elif fromunit=='DECIMAL':
               tovalue=format(int(fromvalue),'b')
          elif fromunit=='OCTAL':
               tovalue=format(int(fromvalue,8),'b')
          elif fromunit=="BINARY":
               tovalue=fromvalue
     if tounit=='DECIMAL':
          if fromunit=='BINARY':
               tovalue=format(int(fromvalue,2),'d')
          elif fromunit=='OCTAL':
               tovalue=format(int(fromvalue,8),'d')
          elif fromunit=='HEXADECIMAL':
               tovalue=format(int(fromvalue,16),'d')
          elif fromunit=='DECIMAL':
               tovalue=fromvalue
     if tounit=='OCTAL':
          if fromunit=='BINARY':
               tovalue=format(int(fromvalue,2),'o')
          elif fromunit=='DECIMAL':
               tovalue=format(int(fromvalue),'o')
          elif fromunit=='HEXADECIMAL':
               tovalue=format(int(fromvalue,16),'o')
          elif fromunit=='OCTAL':
               tovalue=fromvalue
     if tounit=='HEXADECIMAL':
          if fromunit=='BINARY':
               tovalue=format(int(fromvalue,2),'x')
          elif fromunit=='DECIMAL':
               tovalue=format(int(fromvalue),'x')
          elif fromunit=='OCTAL':
               tovalue=format(int(fromvalue,8),'x')
          elif fromunit=='HEXADECIMAL':
               tovalue=fromvalue
     print(fromvalue,fromunit,tovalue,tounit)
     params={'fv':fromvalue,'fu':fromunit,'tv':tovalue,'tu':tounit}
     return render(request,'numbersystemprocess.html',params)
def power(request):
     return render(request,'power.html')
def powerprocess(request):
     fromvalue=request.POST.get('from')
     fromunit=request.POST.get('power')
     tounit=request.POST.get('powerto')
     fromvalue=float(fromvalue)
     if tounit=='W':
          if fromunit=='Mw':
               tovalue=fromvalue*1000000
          elif fromunit=='Gw':
               tovalue=fromvalue*1000000000
          elif fromunit=='Tw':
               tovalue=fromvalue*1000000000000
          elif fromunit=='Hp':
               tovalue=fromvalue*745.7
          elif fromunit=='W':
               tovalue=fromvalue
     elif tounit=='Mw':
          if fromunit=='W':
               tovalue=fromvalue/1000000
          elif fromunit=='Gw':
               tovalue=fromvalue*1000
          elif fromunit=='Tw':
               tovalue=fromvalue*1000000
          elif fromunit=='Hp':
               tovalue=fromvalue*0.0007457
          elif fromunit=='Mw':
               tovalue=fromvalue
     elif tounit=='Gw':
          if fromunit=='W':
               tovalue=fromvalue/1000000000
          elif fromunit=='Mw':
               tovalue=fromvalue/1000
          elif fromunit=='Tw':
               tovalue=fromvalue*1000
          elif fromunit=='Hp':
               tovalue=fromvalue/1341000
          elif fromunit=='Gw':
               tovalue=fromvalue
     elif tounit=='Tw':
          if fromunit=='W':
               tovalue=fromvalue/1000000000000
          elif fromunit=='Mw':
               tovalue=fromvalue/1000000
          elif fromunit=='Gw':
               tovalue=fromvalue*1000
          elif fromunit=='Hp':
               tovalue=fromvalue/1341000000;
          elif fromunit=='Tw':
               tovalue=fromvalue
     elif tounit=='Tw':
          if fromunit=='W':
               tovalue=fromvalue/1000000000000
          elif fromunit=='Mw':
               tovalue=fromvalue/1000000
          elif fromunit=='Gw':
               tovalue=fromvalue*1000
          elif fromunit=='Hp':
               tovalue=fromvalue/1341000000;
          elif fromunit=='Tw':
               tovalue=fromvalue
     elif tounit=='Hp':
          if fromunit=='W':
               tovalue=fromvalue*0.00134102;
          elif fromunit=='Mw':
               tovalue=fromvalue*1341.02
          elif fromunit=='Gw':
               tovalue=fromvalue*1341000
          elif fromunit=='Tw':
               tovalue=fromvalue*1341000000
          elif fromunit=='Hp':
               tovalue=fromvalue
     print(fromvalue,fromunit,tovalue,tounit)
     params={'fv':fromvalue,'fu':fromunit,'tv':tovalue,'tu':tounit}
     return render(request,'powerprocess.html',params)
def angle(request):
     return render(request,'angle.html')
def angleprocess(request):
     fromvalue=request.POST.get('from')
     fromunit=request.POST.get('angle')
     tounit=request.POST.get('angleto')
     fromvalue=float(fromvalue)
     if tounit=='Degrees':
          if fromunit=='Radians':
               tovalue=fromvalue*57.29
          elif fromunit=='Revolutions':
               tovalue=fromvalue*360
          elif fromunit=='Degrees':
               tovalue=fromvalue
     elif tounit=='Radians':
          if fromunit=='Degrees':
               tovalue=fromvalue*0.0174533
          elif fromunit=='Revolutions':
               tovalue=fromvalue*6.28319
          elif fromunit=='Radians':
               tovalue=fromvalue
     elif tounit=='Revolutions':
          if fromunit=='Degrees':
               tovalue=fromvalue*0.00277778
          elif fromunit=='Radians':
               tovalue=fromvalue*0.159155
          elif fromunit=='Revolutions':
               tovalue=fromvalue
     params={'fv':fromvalue,'fu':fromunit,'tv':tovalue,'tu':tounit}
     return render(request,'angleprocess.html',params)
def weight(request):
     return render(request,'weight.html')
def weightprocess(request):
     fromvalue=request.POST.get('from')
     fromunit=request.POST.get('weight')
     tounit=request.POST.get('weightto')
     fromvalue=float(fromvalue)
     tovalue=0
     if tounit=='Mg':
          if fromunit=='g':
               tovalue=fromvalue*1000
          elif fromunit=='Kg':
               tovalue=fromvalue*1000000
          elif fromunit=='Ton':
               tovalue=fromvalue*907184740
          elif fromunit=='Lbs':
               tovalue=fromvalue*453592.37
          elif fromunit=='quintal':
               tovalue=fromvalue*100000000.0
          elif fromunit=='Mg':
               tovalue=fromvalue
     elif tounit=='g':
          if fromunit=='Mg':
               tovalue=fromvalue/1000
          elif fromunit=='Kg':
               tovalue=fromvalue*1000
          elif fromunit=='Ton':
               tovalue=fromvalue*907184.74
          elif fromunit=='Lbs':
               tovalue=fromvalue*453.592
          elif fromunit=='quintal':
               tovalue=fromvalue*100000
          elif fromunit=='g':
               tovalue=fromvalue
     elif tounit=='Kg':
          if fromunit=='Mg':
               tovalue=fromvalue/1000000
          elif fromunit=='g':
               tovalue=fromvalue/1000
          elif fromunit=='Ton':
               tovalue=fromvalue*907.185
          elif fromunit=='Lbs':
               tovalue=fromvalue/2.205
          elif fromunit=='quintal':
               tovalue=fromvalue*100
          elif fromunit=='Kg':
               tovalue=fromvalue
     elif tounit=='Ton':
          if fromunit=='Mg':
               tovalue=fromvalue/907184740
          elif fromunit=='g':
               tovalue=fromvalue/907185
          elif fromunit=='Kg':
               tovalue=fromvalue/1000
          elif fromunit=='Lbs':
               tovalue=fromvalue/2000
          elif fromunit=='quintal':
               tovalue=fromvalue/9.072  
          elif fromunit=='Ton':
               tovalue=fromvalue
     elif tounit=='Lbs':
          if fromunit=='Mg':
               tovalue=fromvalue/453592
          elif fromunit=='g':
               tovalue=fromvalue/454
          elif fromunit=='Kg':
               tovalue=fromvalue*2.205
          elif fromunit=='Ton':
               tovalue=fromvalue*2000
          elif fromunit=='quintal':
               tovalue=fromvalue*220.462
          elif fromunit=='Lbs':
               tovalue=fromvalue
     elif tounit=='quintal':
          if fromunit=='Mg':
               tovalue=fromvalue/100000000
          elif fromunit=='g':
               tovalue=fromvalue/100000
          elif fromunit=='Kg':
               tovalue=fromvalue/100
          elif fromunit=='Ton':
               tovalue=fromvalue*9.07185
          elif fromunit=='Lbs':
               tovalue=fromvalue/220
          elif fromunit=='quintal':
               tovalue=fromvalue
     print(fromvalue,tovalue,tounit,fromunit)
     params={'fv':fromvalue,'fu':fromunit,'tv':tovalue,'tu':tounit}
     return render(request,'weightprocess.html',params)
def imagetopdf(request):
     if request.method=="POST":
          img=request.FILES['upload']
          btnvalue=request.POST.get('id')
          print(btnvalue)
          
          print(img.name)
          print(img.size)
          
          #file_url =img.file
          #print(file_url)

          image=Image.open(img)
          print(image.mode)
          if image.mode=="RGBA":
               image=image.convert("RGB")
          output="results\\out.pdf"   
          image.save(output,"PDF",resoultion=300.0)    
     path_on_cloud="images\\comp.jpg"
     path_on_project="media\\comp.jpg"
     storage.child(path_on_cloud).put(path_on_project)  
          #pdf=fitz.open(file_url)
          #page=pdf.loadPage(0)
          #pix=page.getPixmap()
          #pix.writeImage('')
         
          #print(file_url)
          #image = Image.open(r"C:\Users\91738\Desktop\Screenshot 2022-03-01 141707.png")
          #image.save(r'C:\Users\91738\Desktop\convertionj\convertian\results\rees.pdf')
          #pdf_bytes = img2pdf.convert(image.filename)
          #file = open(r"C:\Users\91738\Desktop\convertionj\convertian\results\res.pdf", "wb")
          #file.write(pdf_bytes)
          
          #file.close()
  
     return render(request,'imagetopdf.html')


     
     return render(request,'imagetopdf.html')
def pdftodoc(request):
     if request.method=="POST":
          pdf_file=request.FILES['pdf']
          print(pdf_file.name)
          print(pdf_file.size)
          file_url=pdf_file.file
          doc = aw.Document(file_url)
          doc.save("pdf-to-word.docx")

     return render(request,'pdftodoc.html')

def imagetopdfsuccess(request):
     return render(request,'imagetopdf/imagetopdfsuccess.html')

def doctopdf(request):
     if request.method=="POST":
          word_file=request.FILES['doc']
          file_url=word_file.file
          doc = aw.Document(file_url)
          doc.save("PDF.pdf")

     return render(request,'doctopdf.html')
def home(request):
     return render(request,'index.html')

def compressimage(request):
     if request.method=="POST":
          imgto_c=request.FILES['imgc']
          print(imgto_c.name)
          Image = PIL.Image.open(imgto_c)
          print(Image.size)
          if Image.mode=="RGBA":
               Image=Image.convert("RGB")
               Image.save("media\\input.jpg")
               file_name="media\\comp.jpg"
               Image.save(file_name,optimize=True,quality=1)
          else:
               Image.save("media\\comp.jpg")
               file_name="media\\comp.jpg"
               Image.save(file_name,optimize=True,quality=50)

     path_on_cloud="images\\comp.jpg"
     path_on_project="media\\comp.jpg"
     storage.child(path_on_cloud).put(path_on_project)
          #print(imgto_c.size)
          #if picture.mode=="RGBA":
               #picture=picture.convert("RGB")
            
               #picture.save("C:\\Users\\91738\\Desktop\\convertionj\\convertian\\results\\comp.jpg",optimize=True,quality=30) 
     return render(request,'compressimage.html')