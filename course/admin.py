from django.contrib import admin
from .models import Course, Speciality

admin.site.register(Speciality)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "active_user", "price", "rating")
    list_display_links = ("title", "active_user", "price", "rating")
    prepopulated_fields = {"slug": ("title", "price")}
