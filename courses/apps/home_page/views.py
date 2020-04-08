from django.shortcuts import render
from django.views.generic.base import TemplateView
from ..course_api.models import course_info

def Index(request):
    obj = course_info.objects.all()
    template = 'index.html'
    return render(request, template, {'obj':obj})
