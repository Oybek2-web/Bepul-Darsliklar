from django.db import models
from fanlar.models import Fanlar
from django.utils.translation import gettext_lazy as _

class Darslik(models.Model):
    photo = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name=_('Photo'))
    Video = models.FileField(upload_to="video/", null=True, blank=True)
    Pdf = models.FileField(upload_to="pdf/", null=True, blank=True)
    fan_nomi = models.ForeignKey(Fanlar, on_delete=models.CASCADE, related_name='darsliklar', null=True, verbose_name=_('Fan_nomi'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    describe = models.TextField(verbose_name=_('Describe'))
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "darslik"
