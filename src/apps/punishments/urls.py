from django.urls import path
from . import views


urlpatterns = [
    path('', views.LevelView.as_view(), name='level_list'),
    path('<slug:slug>/', views.LevelDetailView.as_view(), name='level_detail'),
]