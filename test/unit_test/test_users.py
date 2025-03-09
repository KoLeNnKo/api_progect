import allure
import pytest
from config.base_test import BaseTest

class TestUsers(BaseTest):

    @allure.title("Create_Users")
    def test_create_user(self):
        user = self.api_users.create_users()
        self.api_users.get_user_bu_id(user.uuid)