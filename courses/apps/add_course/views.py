from django.shortcuts import render
from rest_framework import viewsets, status
from ..course_api.models import course_info
from ..course_api.serializers import CourseInfoSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

class AddCourseViewSet(viewsets.ModelViewSet):
    queryset = course_info.objects.all()
    serializer_class = CourseInfoSerializer

    

    
