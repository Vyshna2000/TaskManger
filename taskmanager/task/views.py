
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User 
from .models import Tasks
from .forms import TaskForm

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signinform(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use imported login function aliased as auth_login
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    tasks = Tasks.objects.filter(user=request.user)
    search_query = ''
    selected_sort = ''

    if request.method == 'POST':
        if 'search' in request.POST and request.POST['search'].strip():
            search_query = request.POST['search'].strip().lower()
            tasks = tasks.filter(
                title__icontains=search_query
            ) | tasks.filter(
                status__icontains=search_query
            ) | tasks.filter(
                due_date__icontains=search_query
            )

        # Get sorting choice
        selected_sort = request.POST.get('sort_by', '')
        if selected_sort:
            field, direction = selected_sort.split('-')
            field_map = {
                'title': 'title',
                'status': 'status',
                'dueDate': 'due_date',
            }
            order_field = field_map.get(field, 'title')
            ordering = order_field if direction == 'asc' else '-' + order_field
            tasks = tasks.order_by(ordering)
        else:
            tasks = tasks.order_by('-created_at')
    else:
        
        tasks = tasks.order_by('-created_at')

    return render(request, 'dashboard.html', {
        'tasks': tasks,
        'search_query': search_query,
        'selected_sort': selected_sort,
    })


def signup(request):
    return render(request, 'signup.html')


from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

@login_required
def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'signup.html')


        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')

    return render(request, 'signup.html')




def logout(request):
    auth_logout(request)  
    return render(request,'index.html') 


@login_required
def add_task(request):
    form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


@login_required
def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  
            task.user = request.user      
            task.save()                 
            messages.success(request, 'Task added successfully!')
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'task_form.html', {
        'form': form,
        'title': 'Add New Task',
        'button_text': 'Add Task'
    })




@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})



@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('dashboard')
    return redirect('dashboard')



@login_required
def update(request,task_id):
    task = get_object_or_404(Tasks, id=task_id, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('dashboard') 
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form, 'task': task})