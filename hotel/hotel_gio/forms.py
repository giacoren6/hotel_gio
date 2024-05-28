from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room_type', 'check_in', 'check_out', 'guest_name', 'guest_email']
# Compare this snippet from hotel/hotel_gio/views.py: