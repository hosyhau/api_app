from django.db.migrations import serializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from todoapp.models import Todo
from todoapp.permissions import UserIsOwnerTodo
from todoapp.serializers import TodoSerializer

class TodoListCreateApiView(ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_query_set(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self):
        serializer.save(user=self.request.user)

class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = (IsAuthenticated, UserIsOwnerTodo)