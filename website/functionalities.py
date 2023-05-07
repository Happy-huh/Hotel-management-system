from .models import *
import datetime
from django.utils.dateparse import parse_datetime

def check_availability(check_in,check_out,room_type):
    print(check_in)
    check_i = datetime.datetime.strptime(check_in[:10], '%Y-%m-%d')
    check_o = datetime.datetime.strptime(check_out[:10], '%Y-%m-%d')
    available = []
    reservations = Reservation.objects.filter(roomtac=room_type)
    print(reservations)
    for i in reservations:
        i_check_in = str(i.check_in)
        i_check_out = str(i.check_out)
        i_check_in = datetime.datetime.strptime(i_check_in[:10], '%Y-%m-%d')
        i_check_out = datetime.datetime.strptime(i_check_out[:10], '%Y-%m-%d')
        if i_check_in > check_o or i_check_out < check_i:
            available.append(True)
    if all(available) == True:
        return True
    return False

def time_match(check_in,check_out):
    return check_in < check_out