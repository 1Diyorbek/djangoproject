from django.shortcuts import render, redirect
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


class CourseDetailsView(View):
    def get(self, request, slug):
        course = Course.objects.filter(slug=slug)
        context = {
            "course_slug": slug,
            "course": course
        }

        return render(request, "main/course_details.html", context)


class UpdateCourseView(View):
    def get(self, request, slug):
        course = Course.objects.filter(slug=slug)
        context = {
            "course": course
        }
        return render(request, "main/update_course.html", context)

    def post(self, request, slug):
        course = Course.objects.get(slug=slug)
        course.title = request.POST.get('title')
        course.descripiton = request.POST.get('description')
        course.price = request.POST.get('price')
        course.save()
        return redirect("course")
