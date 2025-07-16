from django.urls import path

from .views import HomepageView, CourseCardDetail

urlpatterns = [
    path('home-page/', HomepageView.as_view(), name='homepage-list'),
    path('course-card-detail/<slug:slug>/', CourseCardDetail.as_view(), name='course-card-detail'),
]
