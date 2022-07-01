from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

# register
def registerpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = RegisterPage(request.POST)
            if form.is_valid():
                form.save()
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
                if user is not None:
                    login(request,user)
                    messages.info(request, 'Account Created successfully')
                    return redirect('index')
            else:
                return redirect('register')
        else:
            form = RegisterPage()
            return render(request,'register.html',{'form':form})

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request, 'Invalid Credentials, try again')
                return redirect('login')
        else:
            form = LoginPage()
            return render(request,'login.html',{'form':form})

def logoutpage(request):
    logout(request)
    messages.info(request, 'Logout successfully')
    return redirect('index')

def index(request):
    if request.method == 'POST':
        title = request.POST['searchbar']
        items = Blog.objects.filter(title__icontains=title)
        if title == '':
            messages.info(request, 'Please type something and search')
        else:
            messages.info(request, 'Showing search results for '+ title)
        return render(request, 'index.html',{'items':items})

    else:
        items = Blog.objects.all()
        messages.info(request, 'Latest Tales')
        return render(request, 'index.html',{'items':items})


def detailview(request, pk):
    items = Blog.objects.filter(id=pk)
    post = Blog.objects.get(id=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.post = post
            data.save()
            return redirect('detailview', pk=pk)
    else:
        form = CommentForm()
        return render(request, 'detailview.html',{'items':items,'form':form, 'post':post})


@login_required(login_url= '/login/')
def myblogs(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST['searchbar']
        items = Blog.objects.filter(user=user, title__icontains=title)
        if title is '':
            messages.info(request, 'Please type something and search')
            return render(request,'myblogs.html',{'items':items})
        else:
            messages.info(request, 'Showing results for '+title)
            return render(request,'myblogs.html',{'items':items})
    else:
        user = request.user
        items= Blog.objects.filter(user=user)
        return render(request,'myblogs.html',{'items':items})

@login_required(login_url= '/login/')
def publishblog(request):
    user = request.user
    if request.method == 'POST':
        form = PublishBlog(request.POST, request.FILES)
        if form.is_valid():
            userdata = form.save(commit=False)
            userdata.user = user
            userdata.save()
            messages.info(request, 'Published successfully')
            return redirect('index')
        else:
            return redirect('publish_blog')
    else:
        form = PublishBlog()
        return render(request,'publishblog.html',{'form':form})

@login_required(login_url= '/login/')
def editblog(request, pk):
    blogid = Blog.objects.get(id=pk)
    form = PublishBlog(instance=blogid)

    if request.method == 'POST':
        form = PublishBlog(request.POST, request.FILES, instance=blogid)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated successfully')
            return redirect('my_blogs')
        else:
            return redirect('edit_blog')
    else:
        return render(request,'publishblog.html',{'form':form})

@login_required(login_url= '/login/')
def deleteblog(request, pk):
    blogid =Blog.objects.get(id=pk)

    if request.method == 'POST':
        blogid.delete()
        messages.info(request, 'Deleted successfully')
        return redirect('my_blogs')
    else:
        return render(request,'delete.html',{'blogid':blogid})
