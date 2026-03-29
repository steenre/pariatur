from django.shortcuts import render, redirect
from .models import Post, Category
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AuthenticationForm, PostForm, CategoryForm
from django.contrib.auth import login, authenticate, logout

def siteManager(request):
    if request.user.is_authenticated:
        messages.error(request, 'You cannot be here! You are logged in')
        return redirect('dashboard')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
    
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Login Successful, welcome {username}")
                return redirect('dashboard')
            else:
                form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'panel/login.html', context)


@login_required(login_url='site-manager')
def quitSiteManager(request):
    logout(request)
    messages.success(request, "You logged out successfully!")
    return redirect('posts')

@login_required(login_url='site-manager')
def dashboard(request):
    posts = Post.objects.all()
    post_count = posts.count()
    categories = Category.objects.all()
    categories_count = categories.count()
    context = {
        'posts': posts,
        'categories': categories,
        'post_count': post_count,
        'categories_count': categories_count
    }
    return render(request, 'panel/dashboard.html', context)

@login_required(login_url='site-manager')
def create(request):
    if request.user.is_superuser == False:
        ban = request.user
        ban.is_active = False
        ban.save()
        messages.error(request, "What tha hell are you doing here! You have been banned!")
        return redirect('posts')
    page_name = "Create Post"
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            added = form.save(commit=False)
            added.author = request.user
            try:
                if request.user.is_superuser:
                    added.save()
                    messages.success(request, f"You created {added.title} successfully!")
                    return redirect('manage')
                else:
                    messages.error(request, "What tha fuck are you doing here!")
                    return redirect('posts')
            except Exception as e:
                messages.error(request, "Well, you cannot perform this action")
        else:
            messages.error(request, "Something went wrong, kindly check the form!")
            
    context = {
        'form': form,
        'page_name': page_name
    }
    return render(request, 'panel/create.html', context)

@login_required(login_url='site-manager')
def createCategory(request):
    if request.user.is_superuser == False:
        ban = request.user
        ban.is_active = False
        ban.save()
        messages.error(request, "What tha hell are you doing here! You have been banned!")
        return redirect('posts')
    page_name = "Create Category"
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"You created {form.cleaned_data['cat_name']} successfully!")
                return redirect('manage')
            except Exception as e:
                messages.error(request, f"Well, you cannot perform this action because {e}")
        else:
            messages.error(request, "Something went wrong, kindly check the form!")
            
    context = {
        'form': form,
        'page_name': page_name
    }
    return render(request, 'panel/create.html', context)

@login_required(login_url='site-manager')
def editCategory(request, cat_name):
    if request.user.is_superuser == False:
        ban = request.user
        ban.is_active = False
        ban.save()
        messages.error(request, "What tha hell are you doing here! You have been banned!")
        return redirect('posts')
    page_name = "Edit Category"
    category = Category.objects.get(cat_name=cat_name)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f"You edited {request.POST['cat_name']} successfully!")
            return redirect('manage')
    context = {
        'category':category,
        'form': form,
        'page_name': page_name
    }
    return render(request, 'panel/edit.html', context)

@login_required(login_url='site-manager')
def edit(request, slug):
    if request.user.is_superuser == False:
        ban = request.user
        ban.is_active = False
        ban.save()
        messages.error(request, "What tha hell are you doing here! You have been banned!")
        return redirect('posts')
    page_name = "Edit Post"
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f"You edited {request.POST['title']} successfully!")
            return redirect('manage')
    context = {
        'post':post,
        'form': form,
        'page_name': page_name
    }
    return render(request, 'panel/edit.html', context)

@login_required(login_url='site-manager')
def remove(request, slug):
    if request.user.is_superuser == False:
        ban = request.user
        ban.is_active = False
        ban.save()
        messages.error(request, "What tha hell are you doing here! You have been banned!")
        return redirect('posts')
    page_name = "Post"
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        try:
            post.delete()
            messages.success(request, f"You deleted {post.title}")
        except Exception as e:
            messages.error(request, f"{e}")
        return redirect('dashboard')
    context = {
        'post':post,
        'page_name': page_name
    }
    return render(request, 'panel/remove.html', context)

@login_required(login_url='site-manager')
def removeCategory(request, cat_name):
    if request.user.is_superuser == False:
        ban = request.user
        ban.is_active = False
        ban.save()
        messages.error(request, "What tha hell are you doing here! You have been banned!")
        return redirect('posts')
    page_name = "Category"
    category = Category.objects.get(cat_name=cat_name)
    cat_count = Post.objects.filter(category=category).count()
    if request.method == 'POST':
        try:
            category.delete()
            messages.success(request, f"You deleted {category.cat_name}")
        except Exception as e:
            messages.error(request, f"{e}")
        return redirect('dashboard')
    context = {
        'category':category,
        'page_name': page_name,
        'cat_count':cat_count
    }
    return render(request, 'panel/remove.html', context)

@login_required(login_url='site-manager')
def manage(request):
    if request.user.is_superuser == False:
        ban = request.user
        ban.is_active = False
        ban.save()
        messages.error(request, "What tha hell are you doing here! You have been banned!")
        return redirect('posts')
    posts = Post.objects.all()
    cats = Category.objects.all()
    post_count = posts.count()
    context = {
        'posts': posts,
        'cats': cats,
        'post_count': post_count
    }
    return render(request, 'panel/manage.html', context)