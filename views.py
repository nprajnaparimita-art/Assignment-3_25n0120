from rest_framework import generics, permissions
from .models import Bounty
from .serializers import BountySerializer, UserSerializer
from django.contrib.auth.models import User

# Register User
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# List all bounties and create a new bounty
class BountyListCreateView(generics.ListCreateAPIView):
    serializer_class = BountySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bounty.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Retrieve, Update and Delete a bounty
class BountyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BountySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Bounty.objects.filter(owner=self.request.user)