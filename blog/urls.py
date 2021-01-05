from django.urls import path, include
from .views import HomeView, BlogDetailsView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('details/<int:pk>', BlogDetailsView.as_view(), name='blog_details'),
    path('add/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),
]

