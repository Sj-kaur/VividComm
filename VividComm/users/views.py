from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token # For Token Authentication
from django.contrib.auth import authenticate, login, logout # Import logout too
from .serializers import UserSerializer, LoginSerializer, UserProfileSerializer
from .models import CustomUser


from .serializers import UserSerializer, LoginSerializer
from .models import CustomUser # Ensure CustomUser is imported


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    # Allow any user (even unauthenticated) to access this endpoint for registration
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class LoginView(APIView):
    # Allow any user to access this endpoint for login
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer # We're using a specific serializer for login input

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True) # Validate input data

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        # Authenticate the user using Django's built-in authenticate function
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication is successful, log the user in (creates a session)
            login(request, user)
            # Get or create a DRF authentication token for the user
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'message': 'Login successful',
                'token': token.key, # Return the token to the client
                'user_id': user.id,
                'username': user.username,
                'email': user.email, # Add user details if needed
            }, status=status.HTTP_200_OK)
        else:
            # If authentication fails
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    # Only authenticated users can access this endpoint
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        # Django's logout function invalidates the session
        logout(request)
        # If using Token authentication, delete the token
        if hasattr(request.user, 'auth_token'):
            request.user.auth_token.delete()
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
    
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # This ensures that a user can only view/update their own profile
        return self.request.user