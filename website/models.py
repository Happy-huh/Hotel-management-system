from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        
class Post(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    picture = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    @property
    def imageURL(self):
        try:
            img = self.picture.url
        except:
            img = ' '
        return img

    def __str__(self):
        return self.name
    

class Room(models.Model):
    name = models.CharField(max_length=200)
    main_picture = models.ImageField(null=True, blank=True)
    price = models.IntegerField(null=True,blank=True)
    description = models.TextField()
    beds = models.IntegerField(null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    
    @property
    def imageURL(self):
        try:
            img = self.main_picture.url
        except:
            img = ' '
        return img

    def __str__(self):
        return self.name

class Roomtac(models.Model):
    number = models.IntegerField()
    category = models.ForeignKey(Room,on_delete=models.CASCADE)
    category_number = models.IntegerField()

    def __str__(self):
        name = self.category.name
        return f'{name} room {self.number}'

class Roompicture(models.Model):
    image = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=300)
    room = models.OneToOneField(Room, on_delete=models.CASCADE, blank=True, null=True)
    roomtac = models.ForeignKey(Roomtac,on_delete=models.CASCADE, null=True, blank=True)
    children = models.BooleanField(null=True, blank=True, default=False)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    number_of_people = models.IntegerField(null=True, blank=True)
    number_of_children = models.IntegerField(null=True, blank=True)
    extra_request = models.TextField(null=True, blank=True)
    date_booked = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.fullname} booked {self.room} on {self.check_in}'