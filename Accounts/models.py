from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

USER_TYPE_CHOICES = (
    ('admin', 'admin'),
    ('doctor', 'doctor'),
    ('patient', 'patient'),
    ('staff', 'staff'),
    ('user_admin', 'user_admin'),
)

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))
        '''
        One application of normalizing emails is to prevent multiple signups.
         If your application lets the public to sign up,
          your application might attract the "unkind" types
        '''
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, **other_fields)
        #password must be stored using set_password() method
        user.set_password(password)

        user.save()
        return user

#class NewUser that is inherited from AbstractBaseUser
class NewUser(AbstractBaseUser, PermissionsMixin):
    #_('email address') is Label
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True,null=True)
    last_name = models.CharField(max_length=150, blank=True,null=True)
    #password2 field to ensure that password is correct
    password2 = models.CharField(max_length=120)
    Address = models.CharField(max_length=300)
    Contact = models.CharField(max_length=25)
    BirthDate =models.DateField(auto_now=False, blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)


    user_type = models.CharField(max_length=40, choices=USER_TYPE_CHOICES ,default=USER_TYPE_CHOICES[3][1],blank=True,null=True)

    #fields to know if user patient or doctor or admin and this fields will be updated
    #in all classes inherited from user class
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    objects = CustomAccountManager()

    #instead of username field it will take email field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return self.username

#the job of this Method is to create Token Automatically when event occured
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

    for user in NewUser.objects.all():
        Token.objects.get_or_create(user=user)



