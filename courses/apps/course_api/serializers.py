from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import course_info

class CourseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = course_info
        fields = '__all__'
    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']