from django.shortcuts import render, redirect
from .models import *
from .functionalities import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import *
from django.utils import timezone

# Create your views here.
def home_page(request):
    rooms = Room.objects.all()
    context = {
        'rooms':rooms,
    }
    return render(request, 'website/home.html', context)

def gallery(request):
    return render(request, 'website/gallery.html')
    
def blog(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    context = {
        'categories':categories,
        "posts":posts,
    }
    return render(request, 'website/blog.html', context)

def blog_category(request, category_pk):
    try:    
        categories = Category.objects.all()
        category = Category.objects.get(id=category_pk)
        posts = category.post_set.all()
        context = {
            'categories':categories,
            "posts":posts,
        }
        return render(request, 'website/blog.html', context)
    except:
        return render(request, 'website/blog.html')
    
def blog_post(request, post_pk):
    try:
        post = Post.objects.get(id=post_pk)
        context = {
            'post':post,
        }
        return render(request, 'website/blog_post.html', context)
    except:
        return render(request, 'website/blog.html')

    
def rooms(request):
    rooms = Room.objects.all()
    context = {
        'rooms':rooms,
    }
    return render(request, 'website/rooms.html', context)
    
def specific_room(request, room_pk):
    try:
        reservationsForm = ReservationsForm()
        room = Room.objects.get(id=room_pk)
        context = {
            'room':room,
            'reservationsForm':reservationsForm,
        }
        return render(request, 'website/specific_room.html', context)
    except:
        return render(request, 'website/rooms.html')
    
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'website/signup.html', {'form':form})
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'website/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        pass

@login_required(login_url="/signUp/")
def bookings(request):
    user = request.user
    if request.method == 'POST':
        data = request.POST
        check_in = data['check_in']
        check_out = data['check_out']
        room_type = data['room']
        fullname = data['fullname']
        rooms = Roomtac.objects.filter(category=room_type)
        success_message = False
        message = True
        form = ReservationsForm(request.POST)
        ans = []
        
        for room in rooms:
            if time_match(check_in,check_out) and check_availability(check_in,check_out,room):
                ans.append(room)
        
        if time_match(check_in,check_out) and check_availability(check_in,check_out,ans[0]):
            if form.is_valid():
                form.save()
                reservate = Reservation.objects.get(fullname=fullname,check_in=check_in,check_out=check_out,room=room_type)
                reservate.roomtac = ans[0]
                reservate.user = user
                reservate.save()
                message = False
                success_message = True

        context = {
            'success_message':success_message,
            'message': message,
            'form':form,
        }
    else:
        form = ReservationsForm()
        message = False
        success_message = False
        context = {
            'success_message':success_message,
            'message': message,
            'form':form,
        }
    return render(request, 'website/booking.html', context)

@login_required(login_url = '/signUp/')
def cart(request):
    user = request.user
    bookings = Reservation.objects.filter(user=user)
    available_bookings = []
    time = timezone.now()
    for i in bookings:
        if i.check_out > time:
            available_bookings.append(i)
    if len(available_bookings) < 1:
        empty = True
    else:
        empty=False

    context = {
        'empty':empty,
        'reservations':available_bookings,
    }
    return render(request, 'website/cart.html', context)

def reservation(request,reservation_pk):
    try:
        reservate = Reservation.objects.get(pk=reservation_pk)
        context = {
            'reservation':reservate,
        }
        return render(request, 'website/reservation.html', context)
    except:
        return render(request, 'website/cart.html')