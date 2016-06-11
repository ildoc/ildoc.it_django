import os
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from markdown import markdown

from django.conf import settings
from blog.models import Post


def is_absolute(url):
    return bool(urllib.parse.urlparse(url).netloc)

posts = Post.objects.all()
image_folder = os.path.join(settings.BASE_DIR, "static\\images\\posts")


for post in posts:
    imgs = BeautifulSoup(post.content_html).findAll('img')
    for img in imgs:
        imgurl = img['src']
        if is_absolute(imgurl):
            print(imgurl)
            urllib.request.urlretrieve(imgurl, os.path.join(image_folder, os.path.join(image_folder, imgurl.split('/')[-1])))
            print('salvata')
