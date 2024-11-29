from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm


def home(request):
    return render(request, 'home.html')

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            messages.success(request, "Your service request has been submitted successfully!")
            service_request.save()
            return redirect('home')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

def dashboard(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'dashboard.html', {'requests': requests})

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            
            user = authenticate(request, username=username, password=password)
            if user is not None:  
                login(request, user)  
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('admin_dashboard')  
            else:
                messages.error(request, "Invalid username or password.")  
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')

def admin_dashboard(request):
    if not request.user.is_authenticated:  
        messages.error(request, "Please log in to access the admin dashboard.")
        return redirect('login')

    if request.method == 'POST':
        for req in ServiceRequest.objects.all():
            new_status = request.POST.get(f"status_{req.id}")
            if new_status and req.status != new_status:
                req.status = new_status
                req.save()
        messages.success(request, "Status updated successfully!")
        return redirect('admin_dashboard')

    
    service_requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'admin_dashboard.html', {'service_requests': service_requests})