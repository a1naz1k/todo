from rest_framework import viewsets,permissions
from .serializer import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import *
from rest_framework.filters import SearchFilter

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class =TaskFilter
    search_fields = ['task']
    permission_classes =[permissions.IsAuthenticated]