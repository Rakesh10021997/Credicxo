from django.db import models

# Create your models here.
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class UsersCommanFields(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    phone = models.CharField(max_length=10, default="1234567899")
    address = models.CharField(max_length=200, blank=True)
    class Meta:
        abstract = True

class Teacher(UsersCommanFields):
    qualification = models.CharField(max_length=100, default="None")
    def __str__(self):
        return self.user.username


# ------------------------------------Student Singup Model-----------------------------------------------
class Student(UsersCommanFields):
    schoolName = models.CharField(max_length=150, default=" ")
    def __str__(self):
        return self.user.username

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )

from django.db import models
class Student_info(models.Model):
    name=models.CharField(max_length=64)
    addr=models.CharField(max_length=64)
