from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
# Create your views here.
def courses(request):
    courses= Course.objects.all()
    paginator = Paginator(courses, 10)
    page = request.GET.get('page')
    courses = paginator.get_page(page)
    context ={
        'courses':courses
    }
    return render(request,'course/course.html',context)

def course_video(request,id):
    course = Course.objects.get(id=id)
    context={
        'course_video': course
    }
    return render(request,'course/course_videos.html',context)
