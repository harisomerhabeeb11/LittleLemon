from django.test import TestCase
from ..models import Menu
from ..serializers import MenuSerializer
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu Model
        Menu.objects.create(title="IceCream", price=7.99, inventory=100)
        Menu.objects.create(title="Pasta}", price=8.99, inventory=100)
        Menu.objects.create(title="Burger", price=9.99, inventory=100)
        Menu.objects.create(title="Pizza", price=9.99, inventory=100)

    def test_getAll(self):
        # Retrieve all Menu objects.
        url = reverse('menu-item-list')  # Update with your actual URL pattern
        client = APIClient()
        response = client.get(url)
        
        # Check if the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the Menu objects
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        # Check if the serialized data matches the response data
        self.assertEqual(response.data, serializer.data)