from django.shortcuts import render
from django.views import View
from .models import Course, Speciality
from teacher.models import Teacher


class LandingPageView(View):
    def get(self, request):

        courses = Course.objects.all()
        specialitys = Speciality.objects.all()
        teachers = Teacher.objects.all()

        context = {
            "courses": courses,
            "specialitys": specialitys,
            "teachers": teachers
        }

        return render(request, "main/index.html", context)


class CoursePageView(View):
    def get(self, request):

        courses = Course.objects.all()
        specialitys = Speciality.objects.all()

        context = {
            "courses": courses,
            "specialitys": specialitys
        }

        return render(request, "main/course.html", context)


class AboutPageView(View):
    def get(self, request):
        return render(request, "main/about.html")


class ContactPageView(View):
    def get(self, request):
        return render(request, "main/contact.html")
