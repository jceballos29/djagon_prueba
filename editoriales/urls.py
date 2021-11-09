from rest_framework.routers import DefaultRouter
from editoriales.views import EditorialViewSet

router = DefaultRouter()
router.register('editoriales', EditorialViewSet)

urlpatterns = router.urls
