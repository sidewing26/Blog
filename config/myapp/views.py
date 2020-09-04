from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from .models import User, Blog

# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else :
            return render(request, 'index.html', {'error' : '아이디 비밀번호 오류'})

    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['passwd1'] == request.POST['passwd2']:
            name = request.POST['name']
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['passwd1'],
                greet=name + '님 로그인 되셨습니다.'
            )
            return redirect('signup_done')
        return render(request, 'signup.html', {'error': '비밀번호 오류'})
    return render(request, 'signup.html')

def signup_done(request):
    return render(request, 'signup_done.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def blog(request):
    blog = Blog.objects.filter(user=request.user)
    return render(request, 'blog.html', {'blog':blog})

def blog_c(request):
    if request.method == 'POST':
        blog = Blog()
        blog.user = request.user
        blog.title = request.POST.get('title')
        blog.contents = request.POST.get('contents')
        blog.save()
    
        return render(request, 'blog_c.html', {'done':'업로드 완료'})
    return render(request, 'blog_c.html')

def blog_d(request):
    blog_id = request.GET['blog_id']
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('blog')

def blog_u(request, pk):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, pk=pk)
        user = request.user
        title = request.POST['title']
        contents = request.POST['contents']
        blog.title = title
        blog.contents = contents
        blog.save()
        return render(request, 'blog_u.html', {'done': '수정하였습니다.', 'blog':blog})

    return render(request, 'blog_u.html')