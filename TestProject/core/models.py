# school/models.py
from django.db import models


class School(models.Model):
    name = models.CharField(max_length=255, db_index=True)  # Indexed for faster search
    address = models.TextField()
    established_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="teachers")
    first_name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100, db_index=True)
    subject = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="students")
    first_name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100, db_index=True)
    roll_number = models.PositiveIntegerField()
    class_name = models.CharField(max_length=50, db_index=True)

    class Meta:
        unique_together = ("school", "roll_number")  # Index for quick lookup
        indexes = [
            models.Index(fields=["class_name", "roll_number"]),  # Composite index
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

