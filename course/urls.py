from django.contrib import admin
from django.urls import path

from course import views

urlpatterns = [
    path('',views.courses,name='courses'),
    path('<int:id>',views.course_video,name='course_video'),
]
