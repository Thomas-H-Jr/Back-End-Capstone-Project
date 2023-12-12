from django.test import TestCase
from django.urls import reverse
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer
from rest_framework import status
from rest_framework.test import APIClient


class MenuViewTest(TestCase):
    def setUp(self):
        # Create some test instances of the Menu model
        Menu.objects.create(title="Item 1", price=10.99, inventory=5)
        Menu.objects.create(title="Item 2", price=15.49, inventory=8)
        Menu.objects.create(title="Item 3", price=7.99, inventory=3)

    def test_getall(self):
        # Retrieve all Menu objects
        client = APIClient()
        url = reverse(
            "restaurant/menu/items"
        )  # Replace 'menu-list' with the actual URL name for listing menus
        response = client.get(url)

        # Check if the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the test instances
        expected_data = MenuSerializer(Menu.objects.all(), many=True).data

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, expected_data)
