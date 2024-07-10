from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random
from .models import User

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    quotes = [
        "The best way to predict the future is to create it.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "In the middle of difficulty lies opportunity.",
        "Believe you can and you're halfway there.",
        "Strive not to be a success, but rather to be of value."
    ]
    quote = random.choice(quotes)
    return render(request, 'index.html', {'now': now, 'quote': quote})


def contact(request):
    return render(request, 'contact.html')

def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        user = User(name=name, email=email)
        user.save()
        return HttpResponse(f"Name: {name}, Email: {email}")
    
def users(request):
    all_users = User.objects.all()
    return render(request, 'users.html', {'users': all_users})



def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        user = User(name=name, email=email, message=message)
        user.save()
        return HttpResponse(f"Thank you {name}, your message has been received.")
    return render(request, 'contact.html')

