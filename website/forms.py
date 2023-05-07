from .models import Reservation
from django import forms

class ReservationsForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields =[
            'fullname',
            'room',
            'check_in',
            'check_out',
            'children',
            'number_of_people',
            'number_of_children',
            'extra_request'
            ]