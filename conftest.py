import pytest

from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.nova_post.main_page_nova_poshta import MainPageNP


class User:

    def __init__(self)-> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Sergii'
        self.second_name = 'Butenko'

    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api


@pytest.fixture
def database():
    db = Database()

    yield db


@pytest.fixture
def nova_post_main_page():
    main_page = MainPageNP()

    yield main_page
