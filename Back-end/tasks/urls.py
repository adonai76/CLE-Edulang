from django.urls import path, include
from rest_framework import routers
from .views import AlumnoViewSet
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register(r'alumnos', AlumnoViewSet, 'alumnos')

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='API de Gestión de Alumnos'))
]
