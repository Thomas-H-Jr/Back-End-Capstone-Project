from django.urls import path
from .views import MenuItemsView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("api-token-auth/", obtain_auth_token),
    path("items/", MenuItemsView.as_view()),
    path("items/<int:pk>", SingleMenuItemView.as_view()),
    # path("booking/", views.BookingView.as_view()),
]
