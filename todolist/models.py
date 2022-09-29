from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ModelForm

class Task(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    date = models.DateField()
    title = models.CharField(max_length=255)
    description= models.TextField()

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
    