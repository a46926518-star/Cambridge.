from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArizaViewSet, SavolViewSet, KursViewSet, NatijaViewSet, SavolJavobViewSet

router = DefaultRouter()
router.register(r'arizalar', ArizaViewSet)
router.register(r'savollar', SavolViewSet)
router.register(r'kurslar', KursViewSet)
router.register(r'natijalar', NatijaViewSet)
router.register(r'savol-javoblar', SavolJavobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]