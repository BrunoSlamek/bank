from rest_framework import routers
from .views import AtivoViewSet, CarteiraViewSet, AplicacaoViewSet

router = routers.DefaultRouter()
router.register(r'ativo', AtivoViewSet)
router.register(r'carteira', CarteiraViewSet)
router.register(r'aplicacao', AplicacaoViewSet)

urlpatterns = router.urls