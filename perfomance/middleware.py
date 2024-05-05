# custom_middleware.py
from rest_framework.authtoken.models import Token
from django.utils.functional import SimpleLazyObject

def get_token(request):
    if not hasattr(request, '_cached_token'):
        tkn = Token.objects.filter(user=request.user).first()
        if tkn:
            request._cached_token = tkn
        else:
            Token.objects.create(user=request.user)
            tkn = Token.objects.filter(user=request.user).first()
            request._cached_token = tkn
            
    return request._cached_token

class TokenHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            token = SimpleLazyObject(lambda: get_token(request))
            request.META['HTTP_AUTHORIZATION'] = f'Token {token.key}'

        response = self.get_response(request)
        return response
