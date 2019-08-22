from rest_framework.viewsets import ModelViewSet
from .serializers import ListSerializer,CardSerializer, ProjectSerializer, UserSerializer
from .models import List, Card, Project
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    def get_queryset(self):
        req = self.request
        new_queryset=[]
        projectid = req.query_params.get('pid')
        if projectid:
            self.queryset = List.objects.filter(project=projectid)
            for list in self.queryset:
                logger.error(str(req.user.username)+" "+str(list.project.userid))
                if str(list.project.userid)==req.user.username:
                    new_queryset.append(list)
            return new_queryset
        else:
            return new_queryset

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all();
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        req = self.request
        projectid = req.query_params.get('pid')
        if projectid:
            self.queryset=Project.objects.filter(id=projectid) 
            return self.queryset
        else:
            return Project.objects.filter(userid=req.user.id)  

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        req = self.request
        return User.objects.filter(id=req.user.id) 
