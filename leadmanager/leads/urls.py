from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
# register routes
router.register('api/leads', LeadViewSet, 'leads')

# give urls registered for this endpoint
urlpatterns = router.urls