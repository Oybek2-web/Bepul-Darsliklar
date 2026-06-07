from django.db import models

class StartUp(models.Model):
    nomi = models.CharField(max_length=255)
    tavsif = models.TextField()
    github_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomi

    class Meta:
        db_table = 'startup'

# Create your models here.
