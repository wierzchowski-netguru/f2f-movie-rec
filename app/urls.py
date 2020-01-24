from django.urls import path

from app.views import MovieTemplateView

urlpatterns = [
    path('', MovieTemplateView.as_view()),
]
