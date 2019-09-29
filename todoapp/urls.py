from django.urls import path
from todoapp.views import TodoListCreateApiView, TodoDetailAPIView

app_name = 'todos'

urlpatterns = [
    path('', TodoListCreateApiView.as_view(), name = "list"),
    path('<int:pk>/', TodoDetailAPIView.as_view(), name="detail"),
]