
from django.urls import path

from char.views import TestView

app_name = 'char'

urlpatterns = [
    path('', TestView.as_view(), name='test'),
]
