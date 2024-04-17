from django.shortcuts import render
from django.views import View
from .models import Teacher


class TeacherPageView(View):
    def get(self, request):

        teachers = Teacher.objects.all()

        context = {
            "teachers": teachers
        }

        return render(request, "main/teacher.html", context)


class BlogPageView(View):
    def get(self, request):

        return render(request, "main/blog.html")
