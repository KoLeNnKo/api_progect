import os

HOST = "https://release-gs.qa-playground.com/api/v1"

class Endpoints:
    create_users = f"{HOST}/users"
    get_user_by_id = lambda self, uuid: f"{HOST}/users/{uuid}"