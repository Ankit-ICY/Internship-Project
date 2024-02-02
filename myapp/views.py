from django.shortcuts import render
from myapp.models import Contact, Quotes
from django.utils import timezone
import random
from validate_email_address import validate_email
import re

# Create your views here.


def home(request):
    current_datetime = timezone.now()
    random_quote = get_random_quote()
    weather_info = get_weather_information()

    # Pass dynamic content to the template
    context = {
        'current_datetime': current_datetime,
        'random_quote': random_quote,
        'weather_info': weather_info,
    }

    return render(request,  'home.html' , context)


def get_random_quote():
    quotes = Quotes.objects.all()
    return random.choice(quotes).quote



def get_weather_information():
    return "Sunny, 25°C"


def contact(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        
    
        if not is_valid_phone_number(number):
            notification = "Invalid Number"
        
        elif is_valid_email(email):
            contact = Contact.objects.create(name=name, email= email ,phone_number = number, message = message)
            contact.save()
            notification ="success"

        else:
            notification = "Invalid Email"

    else:
        notification = None
    context  = {'notification' : notification}
    return render(request,  'contact.html', context)




def users(request):
    users = Contact.objects.all()
    context = {'users' : users}
    return render(request, 'users.html', context)


def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except :
        return False
    


def is_valid_phone_number(phone_number):
    phone_number_pattern = re.compile(r'^\d{10}$')

    return bool(re.match(phone_number_pattern, phone_number))