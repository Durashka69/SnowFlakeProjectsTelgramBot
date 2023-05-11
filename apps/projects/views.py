from rest_framework import generics

from apps.projects.models import Project, Appeal
from apps.projects.serializers import ProjectSerializer, AppealSerializer


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class AppealListCreateAPIView(generics.ListCreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer


class AppealRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
