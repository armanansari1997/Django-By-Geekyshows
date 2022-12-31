
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homefun/', views.homefun, name='homefun'),
    path('homecl/', views.HomeClassView.as_view(), name='homecl'),

    path('aboutfun/', views.aboutfun, name='aboutfun'),
    path('aboutcl/', views.AboutClassView.as_view(), name='aboutcl'),

    path('contactfun/', views.contactfun, name='contactfun'),
    path('contactcl/', views.CotactClassView.as_view(), name='contactcl'),

    path('newsfun/', views.newsfun, {'template_name':'school/news.html'}, name='newsfun'),
    path('newsfun2/', views.newsfun, {'template_name':'school/news2.html'}, name='newsfun2'),
    path('newscl/', views.NewsClassView.as_view(template_name = 'school/news.html'), name='newscl'),
    path('newscl2/', views.NewsClassView.as_view(template_name = 'school/news2.html'), name='newscl2')
]

