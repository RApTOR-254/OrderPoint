from mozilla_django_oidc.auth import OIDCAuthenticationBackend

from api.models import Customer

class CustomOIDCAuthenticationBackend(OIDCAuthenticationBackend):
    def create_user(self, claims):
        """Create a user from Google claims"""
        return Customer.objects.create(
            name = claims.get('name', ''),
            email = claims.get('email', ''),
            sub = claims.get('sub', ''),
            phone_number = '',
        )
    
    def filter_users_by_claims(self, claims):
        email = claims.get('email', '')
        sub = claims.get('sub', '')

        if not email or not sub: 
            return Customer.objects.none()
        
        try:
            return Customer.objects.filter(email__iexact=email, sub__iexact=sub)   #check Customer in the database using unique fields 
        except Customer.DoesNotExist:                                              #email and sub
            return Customer.objects.none()
    
    def update_user(self, user, claims):
        """Update user data from claims"""
        user.name = claims.get('name', user.name)
        user.email = claims.get('email', user.email)
        user.sub = claims.get('sub', user.sub)
        user.save()
        return user