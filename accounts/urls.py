from django.urls import path
from .views import LoginPageView, RegisterPageView

app_name = 'accounts'

urlpatterns = [
    # login url
    path('', LoginPageView.as_view(), name="login"),

    # register url
    path('register/', RegisterPageView.as_view(), name="register"),
]
