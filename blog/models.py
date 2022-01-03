from django.db import models
from django.contrib.auth.models import User

class Post(models.Model): #모델을 상속받아 만듦
    title = models.CharField(max_length=100) #포스트 제목
    content = models.TextField() #내용
    pub_date = models.DateTimeField() #작성일
    modify_date = models.DateTimeField(null=True, blank=True) #수정일
    photo = models.ImageField(upload_to='blog/images/%Y/%m/%d/',
                              null=True, blank=True) #images폴더가 자동 생성

    def __str__(self): #관리자 페이지에서 문자로 출력
        return self.title