from backend_api.views import ContactsViewSet
from rest_framework.routers import DefaultRouter
from backend_api import views

router = DefaultRouter()
router.register(r'contacts', ContactsViewSet, basename='contact')
urlpatterns = router.urls