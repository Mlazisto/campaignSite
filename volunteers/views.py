from django.shortcuts import render, redirect
from .models import Volunteer


def volunteers_view(request):
    """
    View function to display a list of volunteers.

    :param request: HttpRequest object representing the incoming request from the user.
    :type request: django.http.HttpRequest

    :returns: HttpResponse object representing the rendered response containing the list of volunteers.
    :rtype: django.http.HttpResponse
    """
    # Fetch all Volunteer objects from the database
    volunteer_list = Volunteer.objects.all

    # Create a context dictionary to pass the volunteer_list to the template
    context = {'volunteer_list': volunteer_list}

    # Render the 'volunteers.html' template with the volunteer_list in the context
    return render(request, 'volunteers.html', context)



def signup_view(request):
    """
    View function to handle user signup and save the submitted form data.

    :param request: HttpRequest object representing the incoming request from the user.
    :type request: django.http.HttpRequest

    :returns: HttpResponse object representing the response to redirect the user to the 'home' page upon successful signup,
              or render the 'signup.html' template with an empty form for GET requests.
    :rtype: django.http.HttpResponse
    """
    if request.method == 'POST':
        # Retrieve data from the submitted form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        # Create a new Volunteer object and save it to the database
        volunteer = Volunteer(first_name=first_name, last_name=last_name, email=email)
        volunteer.save()

        # Redirect the user to the 'home' page after successful signup
        return redirect('home')
    
    # For GET requests, render the 'signup.html' template with an empty form
    return render(request, 'signup.html')