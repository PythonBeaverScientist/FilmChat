# -*- coding: Windows-1251 -*-

import json
from pydantic import BaseModel


class WelcomeModel(BaseModel):
    site_description: str


class WelcomeClass:
    def __init__(self):
        self.welcome_path: str = 'static/site_description.json'

    def load_welcome_json(self) -> json:
        with open(self.welcome_path, 'r') as welcome_file:
            welcome_json: dict = json.load(welcome_file)
        return welcome_json

    @staticmethod
    def create_welcome_model(json_obj: dict) -> WelcomeModel:
        welcome_model = WelcomeModel(**json_obj)
        return welcome_model


def create_welcome():
    welcome_class = WelcomeClass()
    wel_json: dict = welcome_class.load_welcome_json()
    wel_model: WelcomeModel = welcome_class.create_welcome_model(wel_json)
    return wel_model
