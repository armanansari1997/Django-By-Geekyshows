"""gs139 URL Configuration

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
from django.views.generic import TemplateView
from myapp import views as myauth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='myapp/home.html'), name='home'),
    path('dashboard/', TemplateView.as_view(template_name='myapp/dashboard.html'), name='dashboard'),

    path('login/', myauth_views.MyLoginView.as_view(), name="login"),

    path('logout/', myauth_views.MyLogoutView.as_view(), name="logout"),
    path('changepass/', myauth_views.MyPasswordChangeView.as_view(), name='changepass'), 
    path('changepassdone/', myauth_views.MyPasswordChangeDoneView.as_view(), name='changepassdone'), 

]
