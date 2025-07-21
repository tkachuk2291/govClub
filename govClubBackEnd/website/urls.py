from django.urls import path

from .views import HomepageView, CourseCardDetail, Feedback

urlpatterns = [
    path('home-page/', HomepageView.as_view(), name='homepage-list'),
    path('course-card-detail/<slug:slug>/', CourseCardDetail.as_view(), name='course-card-detail'),
    path('feedback/', Feedback.as_view(), name='feedback'),

]
