from django.shortcuts import render, redirect
from .models import Volunteer


def volunteers_view(request):
    volunteer_list = Volunteer.objects.all
    context = {'volunteer_list': volunteer_list}
    return render(request, 'volunteers.html', context)


def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        volunteer = Volunteer(first_name=first_name, last_name=last_name, email=email)
        volunteer.save()

        return redirect('home')
    
    return render(request, 'signup.html')