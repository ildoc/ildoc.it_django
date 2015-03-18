from datetime import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


STATUS_CHOICES = (
    (1, 'Published'),
    (2, 'Draft'),
    (3, 'Hidden'),
)


class Category(models.Model):
    title = models.CharField('Categoria', max_length=200)
    slug = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug= slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField('Tag', max_length=200)
    slug = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug= slugify(self.title)
        super(Tag, self).save(*args, **kwargs)


class Post(models.Model):
    PUBLISHED = 1
    DRAFT = 2
    HIDDEN = 3

    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (HIDDEN, 'Hidden'),
    )

    title = models.CharField('Titolo',max_length=200)
    content = models.TextField('Contenuto')
    slug = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Pubblicato il',default=datetime.now())
    modified_date = models.DateTimeField('Modificato il',default=datetime.now())
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PUBLISHED)

    def excerpt(self):
        maxChar=250
        if len(self.content)>maxChar:
            return self.content[:maxChar-3] + '...'
        else:
            return self.content[:maxChar]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/' + self.slug

    def save(self, *args, **kwargs):
        self.modified_date = datetime.now()
        if not self.id:
            # Newly created object, so set slug
            self.slug= slugify(self.title)
        super(Post, self).save(*args, **kwargs)
