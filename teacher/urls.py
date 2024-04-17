from django.urls import path
from .views import TeacherPageView, BlogPageView

urlpatterns = [
    path('teacher/', TeacherPageView.as_view(), name="teacher"),
    path('blog/', BlogPageView.as_view(), name="blog"),
]
