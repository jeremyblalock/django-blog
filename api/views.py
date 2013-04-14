from models import Post
from serializers import PostSerializer

from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

class PostItem(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)

    model = Post
    serializer_class = PostSerializer

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrReadOnly,)

    model = Post
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = self.model.objects
        if 'before' in self.request.GET:
            queryset = queryset.filter(id__lt=int(self.request.GET['before']))
        return queryset.order_by('-created')[:2]
