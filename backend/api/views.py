from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import ToDoSerializer
from todo.models import ToDo

class TodoList(generics.ListAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]  # Aplica el permiso IsAuthenticated

    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user).order_by('-created')
