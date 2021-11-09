from rest_framework.routers import DefaultRouter
from libros.views import LibrosViewSet

router = DefaultRouter()
router.register('libros', LibrosViewSet)

urlpatterns = router.urls
