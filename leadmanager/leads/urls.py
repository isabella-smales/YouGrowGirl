from rest_framework import routers
from .api import LeadViewSet
from django.views.generic import TemplateView
from django.urls import path, include

router = routers.DefaultRouter()
# register routes
router.register('api/leads', LeadViewSet, 'leads')

# give urls registered for this endpoint
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')), 
    path('/api', include(router.urls)), 
]

