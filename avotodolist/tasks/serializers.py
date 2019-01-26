from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'label', 'completed', 'parent', 'is_subtask')
        read_only_fields = ('is_subtask',)
