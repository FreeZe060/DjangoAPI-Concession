from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from gestion_concessions.views import ConcessionViewSet, VehiculeViewSet

router = routers.SimpleRouter()
router.register(r'concessions', ConcessionViewSet, basename='concession')

vehicule_router = routers.NestedSimpleRouter(router, r'concessions', lookup='concession')
vehicule_router.register(r'vehicules', VehiculeViewSet, basename='concession-vehicules')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(vehicule_router.urls)),
]
