# school/urls.py
from django.urls import path
from .views import (
    SchoolListCreateView,
    SchoolDetailView,
    TeacherListCreateView,
    StudentListView,
)

urlpatterns = [
    path("schools/", SchoolListCreateView.as_view(), name="school-list-create"),
    path("schools/<int:pk>/", SchoolDetailView.as_view(), name="school-detail"),
    path("schools/<int:school_id>/teachers/", TeacherListCreateView.as_view(), name="teacher-list"),
    path("schools/teachers/", TeacherListCreateView.as_view(), name="teacher-list"),
    path("schools/<int:school_id>/students/", StudentListView.as_view(), name="student-list"),
]
