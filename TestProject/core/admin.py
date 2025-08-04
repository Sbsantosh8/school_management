from django.contrib import admin

# Register your models here.

# school/admin.py
from django.contrib import admin
from .models import School, Teacher, Student


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("id","name", "address", "established_year")
    search_fields = ("name", "address")  # Quick search
    list_filter = ("established_year",)  # Filter by year
    ordering = ("name",)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id","first_name", "last_name", "subject", "school")
    search_fields = ("first_name", "last_name", "subject")
    list_filter = ("subject", "school")
    ordering = ("last_name", "first_name")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id","first_name", "last_name", "roll_number", "class_name", "school")
    search_fields = ("first_name", "last_name", "class_name")
    list_filter = ("class_name", "school")
    ordering = ("class_name", "roll_number")
    # To prevent duplicates based on unique_together
    readonly_fields = ()
