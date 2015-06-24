'''
20/03/2015
tool per migrare da pelican a django
'''

import os, sys
import codecs
import argparse
from time import gmtime, strftime
from os import walk
from os.path import join, abspath, normpath, getmtime
from datetime import datetime

from markdown import markdown


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ildoc.settings")
sys.path.append(BASE_DIR)

# This is so my local_settings.py gets loaded.
os.chdir(BASE_DIR)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone

from blog.models import Post, Category, Tag

parser = argparse.ArgumentParser(description='migrate pelican post to django')
parser.add_argument('-f', '--folder', help='post folder', required=True)
parser.add_argument('-s', '--status', default='published', choices=['published', 'draft', 'hidden'] , help='status')
args = parser.parse_args()

post_list = [normpath(abspath(join(root,name)))
        for root, dirs, files in walk(args.folder)
        for name in files
        if name.endswith((".md"))]

def read_metatags(righe):
    meta = []
    i=0
    while repr(righe[i].encode('utf8')) != repr('\r\n'.encode('utf8')):
        meta.append(righe[i].split(' ', 1))
        i+=1
    d = dict((meta[i][0], meta[i][1].replace('\n','')) for i in range(len(meta)))
    d['Content:'] = ''.join(righe[i+1:])
    return d


for post in post_list:
    with codecs.open(post, encoding='utf-8') as f:
        righe = f.readlines()

    post_metatags = read_metatags(righe)

    titolo = post_metatags['Title:']
    slug = post_metatags['Slug:']
    pub_date = datetime.strptime(post_metatags['Date:'].strip(), '%Y-%m-%d %H:%M')
    tags = [x.strip() for x in post_metatags['Tags:'].split(',')]
    tag_slugs = [slugify(x) for x in tags]
    categoria = post_metatags['Category:']
    content = post_metatags['Content:']

    if args.status == 'published':
        status = Post.PUBLISHED
        if 'Status:' in post_metatags:
            if post_metatags['Status:'].strip().lower() == 'published':
                status = Post.PUBLISHED
            elif post_metatags['Status:'].strip().lower() == 'draft':
                status = Post.DRAFT
            elif post_metatags['Status:'].strip().lower() == 'hidden':
                status = Post.HIDDEN

    #aggiungo le tag
    for tag in tags:
        if Tag.objects.filter(slug=slugify(tag)).count() == 0:
            t = Tag(title=tag, slug=slugify(tag))
            t.save()

    #aggiungo la categoria
    if Category.objects.filter(slug=slugify(categoria)).count() == 0:
        c = Category(title=categoria, slug=slugify(categoria))
        c.save()

    #aggiungo il post
    category = Category.objects.get(slug=slugify(categoria))
    posttags = Tag.objects.filter(slug__in=tag_slugs)
    author = User.objects.all().first()

    if Post.objects.filter(slug=slug).count() == 0:
        p = Post(
            title=titolo,
            content=content,
            pub_date=pub_date,
            category=category,
            author=author,
            status=status
        )
        p.save()
        for posttag in posttags:
            p.tags.add(posttag)

        print('creato : ', titolo)
