from rest_framework import viewsets
from .models import User, Team, Activity
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response['Content-Location'] = 'https://glorious-memory-x5pjwjxx7jrpfprx6-8000.app.github.dev'
        return response

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
