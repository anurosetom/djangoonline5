from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
#inheriting ModelViewSet here
# Create your views here.
from .serializer import TaskSerializer
#TaskSeralizer(is a class in serializer.py)
from .models import Task

class TaskView(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

