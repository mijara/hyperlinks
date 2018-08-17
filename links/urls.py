from django.urls import path

from . import views

app_name = 'landing'

urlpatterns = [
    path('<int:pk>/update/', views.LinkUpdateView.as_view(), name='link_update'),
    path('<int:pk>/delete/', views.LinkDeleteView.as_view(), name='link_delete'),
]
