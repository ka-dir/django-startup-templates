from django.urls import path
from .views import BlankDashboardView, OriginalDashboardView

app_name = 'dashboards'

urlpatterns = [
    # original dashboard
    path('original/', OriginalDashboardView.as_view(), name='original-dashboard'),

    # blank dashboard
    path('blank-dashboard/', BlankDashboardView.as_view(), name='blank-dashboard'),
]


