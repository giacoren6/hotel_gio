from django.shortcuts import render
from .forms import BookingForm
from django.shortcuts import redirect
from .models import Booking
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def rooms(request):
    return render(request, 'rooms.html')

def booking(request):
    return render(request, 'booking.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def book_done(request):
    return render(request, 'book_done.html')

def login_done(request):
    return render(request, 'login_done.html')

def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def booking(request):
    return render(request, 'booking_success.html')

def view_bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'view_bookings.html', {'bookings': bookings})

def book(request):
    return render(request, 'book.html')


from django.shortcuts import render, redirect

# ... your other views ...

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

from django.contrib.auth.decorators import login_required

@login_required
def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})
