from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Article(models.Model):
    title  =models.CharField(_("title"), max_length=50)
    body = models.TextField(_("body"))

    

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title

 