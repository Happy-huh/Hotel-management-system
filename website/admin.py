from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Room)
admin.site.register(Roomtac)
admin.site.register(Roompicture)
admin.site.register(Reservation)