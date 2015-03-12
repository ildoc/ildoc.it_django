from datetime import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField('Categoria', max_length=200)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    title = models.CharField('Titolo',max_length=200)
    content = models.TextField('Contenuto')
    slug = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Pubblicato il',default=datetime.now())
    modified_date = models.DateTimeField('Modificato il',default=datetime.now())
    category = models.ForeignKey(Category)

    def excerpt(self):
        maxChar=250
        if len(self.content)>maxChar:
            return self.content[:maxChar-3] + '...'
        else:
            return self.content[:maxChar]

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug= slugify(self.title)
            self.modified_date = datetime.now()
        super(Post, self).save(*args, **kwargs)
