from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets, routers
from rest_framework.decorators import action
from backend.serializers import UserSerializer, GroupSerializer, PostSerializer, CommentSerializer

from mysite import settings
import os

from backend.models import Post, Comment

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    # queryset = Comment.objects.filter(parent=None) # Don't
    queryset = Comment.objects.all()

    serializer_class = CommentSerializer

    @action(detail=False)
    def roots(self, request):
        queryset = Comment.objects.filter(parent=None)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# View to return the static front-end code
def index(request):
    try:
        with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
            return HttpResponse(f.read())
    except FileNotFoundError:
        return HttpResponse(
            """
            Please build the front-end using cd frontend && npm install && npm run build 
            """,
            status=501,
        )
