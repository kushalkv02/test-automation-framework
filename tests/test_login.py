import pytest
import allure
from pages.login_page import LoginPage
from utils.data_loader import load_test_data

test_data = load_test_data("test_data/users.json")

@allure.feature("Login Feature")
@allure.story("User Login Scenarios")
@pytest.mark.parametrize(
    "user",
    test_data,
    ids=["valid_login", "invalid_user", "invalid_password"]
)
def test_login_data_driven(page, user):
    with allure.step("Open login page"):
        login_page = LoginPage(page)
        login_page.open("https://the-internet.herokuapp.com/login")

    with allure.step("Perform login"):
        login_page.login(user["username"], user["password"])

    with allure.step("Validate result"):
        message = login_page.get_message()

        if user["valid"]:
            assert "secure area" in message.lower()
        else:
            assert "invalid" in message.lower()