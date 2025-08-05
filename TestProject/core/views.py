from django.shortcuts import render

# Create your views here.
# school/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import School, Teacher, Student
from .serializers import SchoolSerializer, TeacherSerializer, StudentSerializer


class SchoolListCreateView(APIView):
    def get(self, request):
        schools = School.objects.all().order_by("name")  # Ordered for index usage
        serializer = SchoolSerializer(schools, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SchoolDetailView(APIView):
    def get(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    def put(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









class StudentListView(APIView):
    def get(self, request, school_id):
        # Index used for filtering on class_name
        class_name = request.query_params.get("class_name")
        students = Student.objects.filter(school_id=school_id)
        if class_name:
            students = students.filter(class_name=class_name)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)





from .models import Teacher
from .serializers import TeacherSerializer
from django.shortcuts import get_object_or_404


class TeacherAPIView(APIView):

    # List all teachers
    def get(self, request):
        teachers = Teacher.objects.all().order_by("last_name")
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create a new teacher
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # school will come from JSON
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDetailAPIView(APIView):

    # Retrieve one teacher
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a teacher
    def put(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a teacher
    def delete(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StudentListCreateList(APIView):

    def get(self, request):
        students=Student.objects.all().order_by("id")
        serializer=StudentSerializer(students, many=True)

        return Response(serializer.data)


    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)