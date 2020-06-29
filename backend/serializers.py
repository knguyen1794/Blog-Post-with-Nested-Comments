from django.contrib.auth.models import User, Group
from rest_framework import serializers
from backend.models import Post, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['post']

class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    reply_set = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'date', 'comment', 'from_post', 'parent', 'reply_set')