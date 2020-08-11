from django.contrib import admin
from django.urls import include, path
from djangoExample import views
from rest_framework import routers
from clientapi.views import ClientViewSet

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)

# Register all urls to be accessible via browser
urlpatterns = [
    path('',include(router.urls)),
    path('', views.welcome),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
    