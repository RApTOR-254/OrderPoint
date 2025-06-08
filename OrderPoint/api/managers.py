from django.contrib.auth.models import BaseUserManager

class CustomerManager(BaseUserManager):
    def create_user(self, name: str, email: str, sub: str, phone_number: str, password=None):
        """Creates and saves a User with the given name, email, sub and phone_number"""

        if not email:
            raise ValueError("User must have an email address")
        if not sub:
            raise ValueError("User must have a sub")
        
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            sub = sub,
            phone_number = phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, name: str, email: str, sub: str, phone_number: str, password=None):
        """Creates a superuser with the given name, email, sub, phone_number and password"""

        user = self.create_user(
            email=email,
            name=name,
            sub=sub,
            phone_number=phone_number,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user