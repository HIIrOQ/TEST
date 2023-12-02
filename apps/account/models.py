from django.db import models



class Task(models.Model):
    title =models.CharField(max_length=100)

    decription =models.TextField()

    completed = models.BooleanField(default=False)

    created =models.DateTimeField(auto_now_add=True)