from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        # extra_fields.setdefault('is_admin', True)
        # if extra_fields.get('is_admin') is not True:
        #     raise ValueError('Superuser must have "is_admin" status set to True')
        user = self.create_user(email, password)
        user.admin = True
        user.save()
        return user