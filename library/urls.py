
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include


from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions




schema_view = get_schema_view(
    openapi.Info(
        title="Lot Auction",
        default_version="v1",
        description="Test swagger v1",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hello@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('mainstore.urls')),
    path('api/auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
