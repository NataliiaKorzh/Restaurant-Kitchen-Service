from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from app.models import Dish, DishType

DISH_LIST_URL = reverse("app:dish-list")
COOK_LIST_URL = reverse("app:cook-list")
DISH_TYPE_LIST_URL = reverse("app:dish-type-list")


class PublicViewTest(TestCase):
    def test_login_required(self):
        urls = [
            DISH_LIST_URL,
            COOK_LIST_URL,
            DISH_TYPE_LIST_URL,
        ]
        for url in urls:
            self.assertNotEqual(
                self.client.get(url).status_code, 200
            )


class PrivateViewTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(
            name="Test dish type"
        )
        Dish.objects.create(
            name="Test dish",
            price=20.50,
            description="Test dish description",
            dish_type=self.dish_type,
        )
        self.test_password = "Test1234"
        self.user = get_user_model().objects.create_user(
            username="admin.test",
            years_of_experience=1,
            first_name="Test_first_name",
            last_name="Test_last_name",
            password=self.test_password
        )
        self.client.force_login(self.user)

    def test_dish_list(self):
        response = self.client.get(DISH_LIST_URL)
        dishes = Dish.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )
        self.assertTemplateUsed(response, "app/dish_list.html")

    def test_dish_type_list(self):
        response = self.client.get(DISH_TYPE_LIST_URL)
        dish_types = DishType.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dishtype_list"]),
            list(dish_types)
        )
        self.assertTemplateUsed(response, "app/dishtype_list.html")

    def test_cook_list(self):
        response = self.client.get(COOK_LIST_URL)
        cooks = get_user_model().objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks)
        )
        self.assertTemplateUsed(response, "app/cook_list.html")
