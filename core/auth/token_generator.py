import datetime 
import jwt

from django.conf import settings


class TokenManager():

    def create_token(self, user_id):
        payload = dict(
            id=user_id,
            exp=datetime.datetime.utcnow() + datetime.timedelta(days=1),
            iat=datetime.datetime.utcnow(),
        )
        token = jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')

        return token