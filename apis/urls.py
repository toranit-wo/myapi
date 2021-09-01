from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apis import views
urlpatterns = [
    path('forehand/', views.ForehandList.as_view()),
    path('forehand/<int:pk>/', views.ForehandDetail.as_view()),
    path('backhand/', views.BackhandList.as_view()),
    path('backhand/<int:pk>/', views.BackhandDetail.as_view())
    ]
urlpatterns = format_suffix_patterns(urlpatterns)