from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('category/<str:category_pk>/', views.blog_category, name='blog_category'),
    path('blog/<str:post_pk>/', views.blog_post, name='blog_post'),
    path('rooms/', views.rooms, name='rooms'),
    path('room/<str:room_pk>/', views.specific_room, name='specific_room'),
    path('bookings/', views.bookings, name='bookings'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login_view, name='login'),
    path('signUp/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('reservation/<str:reservation_pk>/', views.reservation, name='reservation'),
]