from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer


# controller
def project_list_view(request):
    projects = Project.objects.all()  
    return render(request, 'main/projects/project_list.html', {'projects': projects})




# API
class ProjectListView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)