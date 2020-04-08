from django.contrib import admin
from django.urls import include,path
from apps.home_page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='index'),
    path('api/course_info', include('apps.course_api.urls')),
    path('api/add_course', include('apps.add_course.urls')),
]