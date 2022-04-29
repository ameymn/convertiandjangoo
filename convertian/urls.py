"""convertian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import home
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('home/',views.index,name='index'),
    path('length/',views.length,name='length'),
    path('length/lengthprocess',views.lengthprocess,name='lengthprocess'),
    path('area/',views.area,name='area'),
    path('area/areaprocess',views.areaprocess,name='areaprocess'),
    path('volume/',views.volume,name='volume'),
    path('volume/volumeprocess',views.volumeprocess,name='volumeprocess'),
    path('temperature/',views.temperature,name='temperature'),
    path('temperature/temperatureprocess',views.temperatureprocess,name='temperatureprocess'),
    path('pressure/',views.pressure,name='pressure'),
    path('pressure/pressureprocess',views.pressureprocess,name='pressureprocess'),
    path('numbersystem/',views.numbersystem,name='numbersystem'),
    path('numbersystem/numbersystemprocess',views.numbersystemprocess,name='numbersystemprocess'),
    path('power/',views.power,name='power'),
    path('power/powerprocess',views.powerprocess,name='powerprocess'),
    path('angle/',views.angle,name='angle'),
    path('angle/angleprocess',views.angleprocess,name='angleprocess'),
    path('weight/',views.weight,name='weight'),
    path('weight/weightprocess',views.weightprocess,name='weightprocess'),
    path('currency/',views.currency,name='currency'),
    path('currency/currencyprocess',views.currencyprocess,name='currencyprocess'),
    path('imagetopdf/',views.imagetopdf,name='imagetopdf'),
    path('pdftodoc/',views.pdftodoc,name='pdftodoc'),
    path('doctopdf/',views.doctopdf,name='doctopdf'),
    path('compressimage/',views.compressimage,name='compressimage'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('postsign/',views.postsign,name='signin'),
    path('postsignup/',views.postsignup,name='postsignup'),
    path('imagetopdfsuccess/',views.imagetopdfsuccess,name='imagetopdfsuccess'),
    #path("upload", views.upload, name="upload"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
