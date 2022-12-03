from django.shortcuts import render , redirect
from .forms import RegisterForm
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
def home(request):
    if request.method == 'POST':
        User = request.user
        date_of_visit = User.date_of_visit
        last_date_of_visit = User.last_date_of_visit
        today = datetime.date.today()
        User.last_date_of_visit = User.date_of_visit
        User.date_of_visit = today
        User.save()

        context = {
            ''
        }

        return render(request, 'main/home.html')
    else:
        return render(request , 'main/home.html')

def update(request):
    User = request.user
    date_of_visit = User.date_of_visit
    last_date_of_visit = User.last_date_of_visit
    # print(User.username)
    # print(User.date_of_visit)
    # print(User.last_date_of_visit)
    return render(request, '')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request , 'registration/sign_up.html' , {"form": form })

