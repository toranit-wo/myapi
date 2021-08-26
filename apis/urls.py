from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apis import views
urlpatterns = [
    path('apis/', views.ApisList.as_view()),
    path('apis/<int:pk>/', views.ApisDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)