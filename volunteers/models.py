from django.db import models

# Create your models here.

class Volunteer(models.Model):
    """
    Model representing a Volunteer.

    :param first_name: First name of the volunteer.
    :type first_name: str

    :param last_name: Last name of the volunteer.
    :type last_name: str

    :param email: Email address of the volunteer.
    :type email: str

    :returns: A string representation of the Volunteer object, displaying their full name.
    :rtype: str
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        """
        Return a string representation of the Volunteer object.

        :returns: The full name of the volunteer.
        :rtype: str
        """
        return (f"{self.first_name} {self.last_name}")
