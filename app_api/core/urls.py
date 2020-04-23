from django.urls import path
from rest_framework import routers

from core.api.views import (AppViewSet,
                            AppApiKeyUpdateView,
                            RetrieveAppByApiKeyView)


router = routers.SimpleRouter()
router.register(r'app', AppViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('update_key/<int:pk>/', AppApiKeyUpdateView.as_view(), name='update-key'),
    path('test/<str:api_key>/', RetrieveAppByApiKeyView.as_view(), name='app-api-key')
]
