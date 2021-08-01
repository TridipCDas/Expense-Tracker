from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self,username,email,password,**extra_fields):

        if username is None:
            raise ValueError("User should have a username")

        if email is None:
            raise ValueError("User should have an email")

        user = self.model(username = username,email = self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self,username,email,password,**extra_fields):

        if password is None:
            raise ValueError("Password field cannot be None")

        user = self.create_user(username,email,password,**extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user