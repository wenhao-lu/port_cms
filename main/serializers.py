from rest_framework import serializers
from .models import Project, Work, Education, Stack

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'  

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'  

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'  

class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = '__all__'  
