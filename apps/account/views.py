from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .TASKserializers import TaskSerializer
from .models import Task
from rest_framework.generics import *


class TaskDetailAPIview(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

class TaskListAPIview(ListCreateAPIView):
    serializer_class = TaskSerializer
    model = Task
    queryset = Task.objects.all()