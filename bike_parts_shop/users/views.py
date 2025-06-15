# # users/views.py
# from django.contrib.auth import login, authenticate
# from django.shortcuts import render, redirect
# from .forms import UserCreationForm

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('/')
#     return render(request, 'users/login.html')

# def register_view(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/login/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/register.html', {'form': form})


from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout

from .serializers import RegisterSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # блокируем refresh-токен
        try:
            token = request.data["refresh"]
            RefreshToken(token).blacklist()
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # чистим сессионный logout (опционально)
        logout(request)
        return Response(status=status.HTTP_205_RESET_CONTENT)

