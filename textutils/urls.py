"""#1 textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

# for video 6:
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.displayTxt, name="displayTxt"),
    path("index/", views.index, name = "index" ),
    path("exc1/", views.exc1, name = "exc1" ),
    path("about/", views.about, name = "about" ),
] """


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("index/", views.index, name = "index" ),
    path("analyze/", views.analyze, name = "analyze" ),

    # path("removePunc/", views.removePunc, name = "removePunc" ),
    # path("capatilizeFirst/", views.capatilizeFirst, name = "capatilizeFirst" ),
    # path("spaceRemove/", views.spaceRemove, name = "spaceRemove" ),
    # path("charCount/", views.charCount, name = "charCount" ),
]
