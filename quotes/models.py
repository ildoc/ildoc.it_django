from django.db import models

from core.models import BaseModel


class Quote(BaseModel):
    text = models.TextField('Testo')
    author = models.CharField('Autore', max_length=200)
    url = models.CharField('Url', max_length=200, blank=True)

    def __unicode__(self):
        return self.text
