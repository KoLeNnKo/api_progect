import allure
import requests
from services.users.models.user_model import UserModel
from utils.helper import Helper
from services.users.endpoints import Endpoints
from services.users.payloads import Payloads
from config.headers import Headers

class UsersAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Создание пользователя")
    def create_users(self):
        response = requests.post(
            url=self.endpoints.create_users,
            headers=self.headers.basic,
            json=self.payloads.create_user
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("Получение пользователя")
    def get_user_bu_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_id(uuid),
            headers=self.headers.basic,
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model