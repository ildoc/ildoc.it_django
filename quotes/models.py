from django.db import models

from core.models import BaseModel


class Quote(BaseModel):
    text = models.TextField('Testo')
    author = models.CharField('Autore', max_length=200)
    url = models.CharField('Url', max_length=200, blank=True)

    def excerpt(self):
        maxChar = 100
        if len(self.text) > maxChar:
            return self.text[:maxChar - 3] + '...'
        else:
            return self.text[:maxChar]

    def __str__(self):
        return self.excerpt()
