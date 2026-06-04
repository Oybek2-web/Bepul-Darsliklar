from django.db import models
from fanlar.models import Fanlar

class Darslik(models.Model):
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    video = models.FileField(upload_to="video/", null=True, blank=True)
    pdf = models.FileField(upload_to="pdf/", null=True, blank=True)
    fan_nomi = models.ForeignKey(Fanlar, on_delete=models.CASCADE, related_name='darsliklar', null=True)
    title = models.CharField(max_length=255)
    describe = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "darslik"
