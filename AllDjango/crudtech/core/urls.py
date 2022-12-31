from django.urls import path
from core import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('addstudent/', views.AddStudent.as_view(), name='addstudent'),
    path('deletestudent/', views.DeleteStudent.as_view(), name='deletestudent'),
    path('updatestudent/<int:id>/', views.EditStudent.as_view(), name='updatestudent'),
]
