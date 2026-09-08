#  nuilt custom model
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser  

# Create your models here.
#Django me Manager ek interface/medium hai jiske through hum database ke model ke objects ke saath kaam karte hain.

class UserManager(BaseUserManager):
    def create_user(self, email, name,tc, password=None , password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc, 
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc ,  password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name = name,
            tc = tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    tc = models.BooleanField() 
    is_active = models.BooleanField(default=True) # Active rhega tb true otherwise false 
    is_admin = models.BooleanField(default=False)  # esko false esiliye quki koi agr login ho toh admin n bn jaye..
    created_at = models.DateTimeField(auto_now_add=True) # jb user creat hoga uss tym ke liye 
    updated_at = models.DateTimeField(auto_now=True) # jb update hoga tb ..   

    objects = UserManager()  # Here are mentioned the usermanager  

    USERNAME_FIELD = "email" # email se login hoga 
    REQUIRED_FIELDS = ['name','tc'] 

    def __str__(self):
        return self.email # jbbhi khi bhi ess obj ko dikhana hoga tb hm usse email ke through hi dikhayenge ..
     
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always ,  give permission only when if user is admin otherwise no permission graunted 
        return self.is_admin 

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
 