from django.urls import path
from .views import LandingPageView, CoursePageView, AboutPageView, ContactPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name="landing"),
    path('course/', CoursePageView.as_view(), name="course"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('contact/', ContactPageView.as_view(), name="contact"),
]
