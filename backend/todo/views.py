from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serilizers import TodoSerializer
from .models import *

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()