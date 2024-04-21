from django.contrib import admin
from .models import Teacher, Position

admin.site.register(Position)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "position")
    list_display_links = ("first_name", "last_name", "position")
    prepopulated_fields = {"slug": ("first_name", "last_name")}

