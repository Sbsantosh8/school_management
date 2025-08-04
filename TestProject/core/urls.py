# school/urls.py
from django.urls import path
from .views import (
    SchoolListCreateView,
    SchoolDetailView,
TeacherAPIView,
TeacherDetailAPIView,
    StudentListView,
)

urlpatterns = [
    path("schools/", SchoolListCreateView.as_view(), name="school-list-create"),
    path("schools/<int:pk>/", SchoolDetailView.as_view(), name="school-detail"),
    path("teachers/", TeacherAPIView.as_view(), name="teacher-list-create"),
    path("teachers/<int:pk>/", TeacherDetailAPIView.as_view(), name="teacher-detail"),
    path("schools/<int:school_id>/students/", StudentListView.as_view(), name="student-list"),
]
