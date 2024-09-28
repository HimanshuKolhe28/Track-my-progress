from django.db import models
from django.contrib.auth.models import User
from django.db import models 


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shortcode = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.user.first_name


class Sprint(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    scrum_master = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class TaskStatus(models.Model):
    title = models.CharField(max_length=100)
    index = models.IntegerField()

    def __str__(self):
        return self.title
    

class Task(models.Model):
    Assign = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True ,blank=True)
    key_id = models.CharField(max_length=10)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE,
            null=True, blank=True,
            help_text="Sprints to organize tasks within a timeframe."
            )
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE,
            null=True, blank=True,
            help_text="Status of the task."
            )
    
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.Assign


'''

    def save(self, *args, **kwargs):
        if not self.pk:
            self.key_id = self.getNextTaskId()
        super().save(*args, **kwargs)

    @staticmethod
    def getNextTaskId():
        INITIAL_TASK_ID = 00000
        instance = Task.objects.order_by("created_at").last()
        return f'SNG_000{str(int(instance.key_id.split("_")[1])+1)}' if not instance is None else f'SNG_000{str(INITIAL_TASK_ID+1)}'
 '''   
  