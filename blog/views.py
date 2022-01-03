from django.shortcuts import render, redirect
from django.utils import timezone
from blog.models import Post
from blog.forms import PostForm

'''
def index(request):
    <연습!!>
    weekday = "금요일"
    weekend = ['토요일', '일요일']
    context = {'day':weekday, 'weekend':weekend}
    return render(request, 'blog/post_list.html', context) #키 값이 넘어간다, html에서 받아준다
    '''

def index(request):
    #블로그 메인 페이지
    post_list = Post.objects.all()
    context = {'post_list':post_list}
    return render(request, 'blog/post_list.html', context)

def post_create(request):
    #글 쓰기 등록
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES) #폼에 입력된 자료 가져오기
        if form.is_valid():
            post = form.save(commit=False) #가 저장
            post.pub_date = timezone.now()
            post.save() #실제 저장
            return redirect('blog:index') #등록 후 블로그 홈으로 이동
    else:
        form = PostForm()
    context = {'form':form}
    return render(request, 'blog/post_form.html', context)

