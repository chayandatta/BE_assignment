from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, status
from .models import course_info
from .serializers import CourseInfoSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class CourseInfoViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = course_info.objects.all()
        serializer = CourseInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = course_info.objects.all()
        courses = get_object_or_404(queryset, pk=pk)
        serializer = CourseInfoSerializer(courses)
        return Response(serializer.data)
    


