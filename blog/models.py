import itertools

from datetime import datetime
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.html import strip_tags

from core.models import BaseModel

from markdown import markdown


class Category(BaseModel):
    title = models.CharField('Categoria', max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Tag(BaseModel):
    title = models.CharField('Tag', max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def count(self):
        return Post.objects.filter(tags=self, status=Post.PUBLISHED).count()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)


class Post(BaseModel):
    PUBLISHED = 1
    DRAFT = 2
    HIDDEN = 3

    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (HIDDEN, 'Hidden'),
    )

    title = models.CharField('Titolo', max_length=200)
    content = models.TextField('Contenuto')
    content_html = models.TextField(editable=False, blank=True, null=True)
    slug = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Pubblicato il', default=timezone.now)
    creation_date = models.DateTimeField('Creato il', default=timezone.now)
    modified_date = models.DateTimeField('Modificato il', default=timezone.now)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PUBLISHED)

    def excerpt(self):
        maxChar = 250
        if len(strip_tags(self.content_html)) > maxChar:
            return strip_tags(self.content_html)[:maxChar - 3] + '...'
        else:
            return strip_tags(self.content_html)[:maxChar]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/' + self.slug

    def is_draft(self):
        return self.status == self.DRAFT

    def save(self, *args, **kwargs):
        self.content_html = markdown(self.content, ['codehilite'])

        if self.status == self.PUBLISHED:
            self.pub_date = datetime.now()

        if not self.id:
            # nuovo oggetto, creo lo slug
            self.slug = orig = slugify(self.title)
            # e mi assicuro che sia univoco
            for x in itertools.count(1):
                if not Post.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (orig, x)

        super(Post, self).save(*args, **kwargs)
