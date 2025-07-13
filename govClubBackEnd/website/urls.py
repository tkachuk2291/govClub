from django.urls import path

from .views import HomepageView
urlpatterns = [
    path('home-page/', HomepageView.as_view())
]
