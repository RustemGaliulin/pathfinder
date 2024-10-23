from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from accounts.views import SignUpView, SignInView

app_name = 'accounts'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
]
