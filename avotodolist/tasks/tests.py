from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

client = APIClient()


class TaskTestCase(TestCase):
    """
    caveat: Testing only subtask related logic because other tests would mean just testing DjangoRestFramework
    """

    def test_subtask_created_successfuly(self):
        task_list_url = reverse('task-list')
        parent_task_response = client.post(task_list_url, {'label': 'dummy parent label text'}, format='json')
        assert parent_task_response.json()['is_subtask'] == False
        parent_task_id = parent_task_response.json()['id']
        parent_url = reverse('task-detail', args=[parent_task_id])

        subtask_response = client.post(task_list_url, {'label': 'dummy sub label text', 'parent': parent_url},
                                       format='json')
        assert subtask_response.json()['is_subtask'] == True
