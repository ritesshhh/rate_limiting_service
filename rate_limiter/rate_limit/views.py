from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rate_limiter.rate_limit.serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from rate_limiter.settings import redis_instance


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        redis_instance.set("user_id", request.user.id)
        serializer_class = self.serializer_class(self.queryset, many=True, context={'request': request})
        print('user logged in :', redis_instance.get("user_id"))
        return Response(serializer_class.data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]