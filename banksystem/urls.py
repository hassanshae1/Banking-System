from django.contrib import admin
from django.urls import include, path, re_path  # Use re_path if you need regex

urlpatterns = [
    path('admin/', admin.site.urls),  # No need for regex here, use path
    path('api-auth/', include('rest_framework.urls')),  # Standard path
    path('api/', include('api.urls')),  # Standard path
]
