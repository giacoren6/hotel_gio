from django.shortcuts import render

# Create your views here.

def hotel_gio(request):
    return render(request, "hotel_gio/hotel_gio.html")
