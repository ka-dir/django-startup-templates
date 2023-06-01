from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('dashboard/', include('dashboards.urls', namespace="dashboards")),
    path('', include('accounts.urls', namespace="accounts")),

   ]
