from django.urls import path
from .views import LandingPageView, CoursePageView, AboutPageView, ContactPageView, UpdateCourseView, CourseDetailsView

urlpatterns = [
    path('', LandingPageView.as_view(), name="landing"),
    path('course/', CoursePageView.as_view(), name="course"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('contact/', ContactPageView.as_view(), name="contact"),
    path('course-details/<slug:slug>', CourseDetailsView.as_view(), name="course_details"),
    path('update-course/<slug:slug>', UpdateCourseView.as_view(), name="update_course"),
]
