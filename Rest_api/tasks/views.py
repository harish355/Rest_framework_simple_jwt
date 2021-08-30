from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *


class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
