from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.

def authenticate_user(request):
    """
    View function to authenticate a user and log them in.

    :param request: HttpRequest object representing the incoming request from the user.
                    This should be a POST request containing the user's username and password.
    :type request: django.http.HttpRequest

    :returns: HttpResponse object representing the response to redirect the user to the 'login' page if the
              authentication fails, or redirect them to the 'home' page if the authentication is successful.
    :rtype: django.http.HttpResponse
    """
    if request.method == 'POST':
        # Retrieve the submitted username and password from the POST request
        username = request.POST['username']
        password = request.POST['password']

        # Attempt to authenticate the user using the provided username and password
        user = authenticate(username=username, password=password)

        # If authentication fails (user is None), redirect the user to the 'login' page
        if user is None:   
            return redirect('user_auth:login')
        else:
            # If authentication is successful, log in the user using Django's 'login' function
            login(request, user)
            # Redirect the user to the 'home' page after successful login
            return redirect('home')


def register_user(request):
    """
    View function to handle user registration.

    :param request: HttpRequest object representing the incoming request from the user.
                    This can be a GET request to load the registration page or a POST request
                    to submit the registration form.
    :type request: django.http.HttpRequest

    :returns: HttpResponse object representing the response to redirect the user to the 'login' page
              after successful registration, or render the 'registration/register.html' template with
              the user registration form for GET requests.
    :rtype: django.http.HttpResponse
    """
    if request.method == 'POST':
        # Create a UserRegistrationForm instance with the submitted form data
        form = UserRegistrationForm(request.POST)

        # Check if the submitted form data is valid
        if form.is_valid():
            # Save the user's registration data to the database
            form.save()

            # Display a success message to the user
            messages.success(request, f'Your account has been created. You can log in now!')

            # Redirect the user to the 'login' page after successful registration  
            return redirect('login')
    else:
        # If the request is a GET request, create an empty UserRegistrationForm instance
        form = UserRegistrationForm()

    # Create a context dictionary to pass the UserRegistrationForm to the template
    context = {'form': form}

    # Render the 'registration/register.html' template with the form in the context
    return render(request, 'registration/register.html', context)


