from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from tasks.models import Task
from tasks.serializers import TaskSerializer


class CsrfDisabledSessionAuthentication(SessionAuthentication):
    """
    Session Authentication with disabled csrf in all cases - specifically useful for dummy projects ;)
    """

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSerializer
    authentication_classes = (CsrfDisabledSessionAuthentication, BasicAuthentication)
