import itertools

from datetime import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils.html import strip_tags

from markdown import markdown


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
    content_html = models.TextField(editable=False, blank=True, null=True)
    slug = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Creato il',default=datetime.now())
    modified_date = models.DateTimeField('Modificato il',default=datetime.now())
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PUBLISHED)

    def excerpt(self):
        maxChar=250
        if len(strip_tags(self.content_html))>maxChar:
            return strip_tags(self.content_html)[:maxChar-3] + '...'
        else:
            return strip_tags(self.content_html)[:maxChar]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/' + self.slug

    def save(self, *args, **kwargs):
        self.modified_date = datetime.now()
        self.content_html = markdown(self.content, ['codehilite'])
        if not self.id:
            # nuovo oggetto, creo lo slug
            self.slug = orig = slugify(self.title)
            # e mi assicuro che sia univoco
            for x in itertools.count(1):
                if not Post.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (orig, x)

        super(Post, self).save(*args, **kwargs)
