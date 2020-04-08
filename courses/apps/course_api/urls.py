from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CourseInfoViewSet

app_name = 'course_information'

router = DefaultRouter(trailing_slash=False)

router.register('', CourseInfoViewSet,
                basename='course_information')


urlpatterns = [
    *router.urls
]