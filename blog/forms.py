from blog.models import Post
from django import forms

#모델하고 연동되는 글 등록 폼 만들기
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo']
        labels = {
            'title': '제목',
            'content': '내용',
            'photo': '사진'
        }
