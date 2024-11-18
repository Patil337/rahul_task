# from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from django.contrib.auth.models import User

# Create your views here.


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(detail=True, methods=["get"])
    def projects(self, request, pk=None):
        client = self.get_object()
        projects = client.projects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# class UserAssignedProjectsView(APIView):
#     def get(self, request):
#         # Example logic for returning user-assigned projects
#         return Response({"message": "This is the UserAssignedProjectsView"})
