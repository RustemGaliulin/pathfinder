from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from accounts.views import SignUpView, SignInView

app_name = 'accounts'

urlpatterns = [
    path('accounts/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('accounts/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/register/', SignUpView.as_view(), name='signup'),
    path('accounts/login/', SignInView.as_view(), name='signin'),
]
