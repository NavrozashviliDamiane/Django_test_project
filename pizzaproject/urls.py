
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from stores.views import UserCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stores.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('register/', UserCreateView.as_view(), name="create_user"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
