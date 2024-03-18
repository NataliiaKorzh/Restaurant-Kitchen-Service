from django.contrib.auth import get_user_model
from django.test import TestCase

from app.forms import (
    DishSearchForm,
    CookCreationForm,
    CookSearchForm,
    DishTypeSearchForm,
)

from app.models import DishType


class FormTests(TestCase):
    def test_form_validity(self):
        form_data = {
            "username": "new_user",
            "password1": "testing123new",
            "password2": "testing123new",
            "years_of_experience": 3,
            "first_name": "Test_first_name",
            "last_name": "Test_last_name",
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data, form_data)


class DishSearchFormTest(TestCase):

    def test_form_validation(self):
        form_valid = DishSearchForm(data={"name": "steak"})
        self.assertTrue(form_valid.is_valid())


class DishTypeSearchFormTest(TestCase):

    def test_form_validation(self):
        form = DishTypeSearchForm(data={"name": "meat"})
        self.assertTrue(form.is_valid())


class CookSearchFormTest(TestCase):

    def test_form_validation(self):
        form_valid = CookSearchForm(
            data={
                "username": "admin1",
                "years_of_experience": 3
            }
        )
        self.assertTrue(form_valid.is_valid())


class DishFormTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="meat")
        self.cook1 = get_user_model().objects.create(
            username="John",
            years_of_experience=3
        )
        self.cook2 = get_user_model().objects.create(
            username="Alice",
            years_of_experience=2
        )
