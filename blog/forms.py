from django.forms import ModelForm, Textarea
from .models import Post, Tag, Category

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags', 'status']
        widgets = {
            'content': Textarea(attrs={'class': 'form-control', 'rows':'3'}),
        }
