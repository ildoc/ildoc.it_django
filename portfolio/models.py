from django.db import models

class Work(models.Model):
    title = models.CharField('Url', max_length=200)
    description = models.TextField('Descrizione')
    #immagine
    url = models.CharField('Url', max_length=200, blank=True)

    def __unicode__(self):
        return self.text
