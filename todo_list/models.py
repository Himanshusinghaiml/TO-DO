from django.db import models

class Todomodel(models.Model):
    Title=models.CharField(max_length=100)
    Description=models.TextField()
    def __str__(self) -> str:
        return self.Title
    
