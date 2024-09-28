from rest_framework import viewsets
from rest_framework.response import Response
from track.models import Profile, Sprint, TaskStatus,Task
from track.serializers import ProfileSerializer, SprintsSerializer, \
    TaskStatusSerializer, TaskSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class SprintsViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintsSerializer  


class TaskStatusViewSet(viewsets.ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer 

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer