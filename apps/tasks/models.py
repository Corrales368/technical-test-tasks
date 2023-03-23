from django.db import models
from django.contrib.auth import get_user_model
from apps.shared.constants import ConstantsCharFields


User = get_user_model()

class Task(models.Model):
    """
    Model to store tasks
    """
    title = models.CharField(max_length=ConstantsCharFields.MAX_LENGTH_SMALL)
    description = models.TextField()
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.pk} {self.title}'
