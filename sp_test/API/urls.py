from django.urls import path
from .views import (
	TestView,
	)

urlpatterns = [
    path('sps/helloworld/v1', TestView.as_view(), name='Products'),
]