from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class LoginView(APIView):
  def post(self, request):
    email = request.data.get('email',None)
    password = request.data.get('password',None)
    user = authenticate(email=email, password=password)

    if user:
      login(request, user)
      return Response(status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_404_NOT_FOUND)
  
class LogoutView(APIView):
  def post(self, request):
      logout(request)

      return Response(status=status.HTTP_200_OK)