from django import forms
from .models import Article, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','image','tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(CommentForm,self).__init__(*args, **kwargs)
        self.fields['content'].label = ""
        self.helper =FormHelper()
        self.helper.layout = Layout(
            Field('content', style='resize:none;', rows='5',id='content'),)

