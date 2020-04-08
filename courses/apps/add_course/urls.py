from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AddCourseViewSet

app_name = 'add_course_information'

router = DefaultRouter(trailing_slash=False)
# router.register('milestones', ProjectMilestonesViewSet,
#                 base_name='project-milestones')
router.register('', AddCourseViewSet,
                basename='add_course_information')


urlpatterns = [
    *router.urls
]