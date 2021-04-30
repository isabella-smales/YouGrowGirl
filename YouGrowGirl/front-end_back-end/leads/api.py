from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset ==> allows us to create CRUD API without explicit methods for functionality
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()  
    permission_classes = [
        permissions.AllowAny
    ]

    # Specifying serializer class 
    serializers_class = LeadSerializer

