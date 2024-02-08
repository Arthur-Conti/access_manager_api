from rest_framework import exceptions


class Validations():

    def validate_user_credentials(self, user, password):
        if user is None:
            raise exceptions.AuthenticationFailed('Invalid Credentials')
        
        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed('Invalid Credentials')
