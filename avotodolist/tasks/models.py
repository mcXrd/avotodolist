from django.db import models


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.TextField(null=False, blank=False)
    completed = models.BooleanField(default=False)

    parent = models.ForeignKey('Task', on_delete=models.SET_NULL, null=True)

    @property
    def is_subtask(self):
        return self.parent is not None
