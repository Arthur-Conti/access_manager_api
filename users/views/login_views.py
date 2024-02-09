from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from users.models import User

from core.auth.token_generator import TokenManager
from core.validations.validations import Validations


class Login(ViewSet):

    token_manager = TokenManager()
    validator = Validations()

    def create(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        self.validator.validate_user_credentials(user, password)

        token = self.token_manager.create_token(user.id)

        resp = Response()
        resp.set_cookie(key='jwt', value=token, httponly=True)

        return resp
