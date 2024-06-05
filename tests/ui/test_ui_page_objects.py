import pytest

from modules.ui.page_objects.nova_post.main_page_nova_poshta import MainPageNP
from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.nova_post.sign_in_nova_poshta import SignInPageNP


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()

    sign_in_page.go_to()

    sign_in_page.try_to_login("page_obj@gmail.com",
                              "wrong_PASSWORD")

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    sign_in_page.close()


@pytest.mark.nova_post_ui
def test_incorrect_username_page_nova_post_object():
    sign_in_page = SignInPageNP()

    sign_in_page.go_to()
    sign_in_page.try_to_login("page_obj@gmail.com",
                              "wrong_PASSWORD")

    assert sign_in_page.check_title("Неправильна електронна адреса чи пароль")

    sign_in_page.close()


@pytest.mark.nova_post_ui
def test_choose_usa_country():
    main_page = MainPageNP()

    main_page.go_to()
    main_page.try_to_choose_usa()

    country = main_page.get_country_title()

    assert "США" == country
