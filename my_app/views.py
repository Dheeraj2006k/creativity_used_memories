from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, PostForm
from django.contrib.auth import authenticate, login, logout
from .models import post
from django.http import HttpResponse
# Create your views here.

def home(request):
    name = "Dheeraj Kumar"
    nums = [1,2,3,4,5]

    context = { 'name' : name , 'age' : 20 , 'nums' : nums }
    return render(request, 'home.html',context)

def user_login(request):
    if request.method == 'GET' :
        return render(request, 'login.html')
    
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
   
        

def registration(request):
    form = UserRegistrationForm() 
    
    if request.method == 'GET' :
        return render(request, 'registration.html', {'form': form})
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'registration.html', {'form': form})

        
    
def user_logout(request):    
    logout(request)
    return redirect('login')

def posts(request):
    post_list = post.objects.all()

    return render(request, 'posts.html',{'post_list' : post_list})

def read_post(request, post_id):
    try:
        post_obj = post.objects.get(id=post_id)
    except post.DoesNotExist:
        return HttpResponse("Post not found.")

    return render(request, 'read_post.html', {'post': post_obj})

def create_post(request):
    form = PostForm()
    if request.method == 'GET':
        return render(request,'create_post.html',{'form' : form})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
       
        if form.is_valid():
            post_obj = form.save(commit=False)
            post_obj.author = request.user
            post_obj.save()
            return redirect('posts')
        else :
            return render(request,'create_post.html',{'form' : form})
        



def update_post(request, post_id):
    try:
        post_obj = post.objects.get(pk=post_id)
    except post.DoesNotExist:
        return HttpResponse("Post not found.")

    if request.user != post_obj.author:
        return HttpResponse("You are not authorized to update this post.")
    
    form = PostForm(instance=post_obj)
    if request.method == 'GET':
        return render(request, 'update_post.html', {'form': form})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post_obj)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            return render(request, 'update_post.html', {'form': form})
        
def delete_post(request, post_id):
    try:
        post_obj = post.objects.get(pk=post_id)
    except post.DoesNotExist:
        return HttpResponse("Post not found.")

    if request.user != post_obj.author:
        return HttpResponse("You are not authorized to delete this post.")
    
    if request.method == 'POST':
        post_obj.delete()
        return redirect('posts')

    return redirect('read_post', post_id=post_id)
