from django.urls import path
from . import views
from .views import MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("api-token-auth/", obtain_auth_token),
    path("", views.index, name="index"),
    path("items/", MenuItemsView.as_view()),
    path("items/<int:pk>", SingleMenuItemView.as_view()),
    # path("booking/", views.BookingView.as_view()),
]
