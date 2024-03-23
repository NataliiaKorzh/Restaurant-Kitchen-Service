from django.contrib.auth import get_user_model
from django.test import TestCase

from app.models import Dish, DishType


class ModelTest(TestCase):
    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="test"
        )
        dish = Dish.objects.create(
            name="Test",
            price=20.50,
            description="test description",
            dish_type=dish_type,
        )
        self.assertEqual(
            str(dish),
            f"{dish.name} {dish_type.name}"
        )

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="test"
        )
        self.assertEqual(str(dish_type), dish_type.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="Test",
            password="Test-password",
            first_name="John",
            last_name="Smith",
            years_of_experience=3,
        )
        self.assertEqual(
            str(cook),
            f"{cook.first_name} {cook.last_name}"
        )
