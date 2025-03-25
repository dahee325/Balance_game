from django.forms import ModelForm
from .models import Article, Comment
from django import forms

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        fields = '__all__'
        # widgets = {
        #     'title' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': '제목을 입력하세요.'}),
        # }


class CommentForm(ModelForm):
    # AB = forms.ChoiceField(widget=forms.Select(), choices=[(1, 'A'), (2, 'B')])
    class Meta():
        model = Comment
        exclude = ('article', )
        widgets = {
            'AB' : forms.Select(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '내용을 입력하세요.'}),
        }