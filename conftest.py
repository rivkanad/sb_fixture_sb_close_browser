import pytest


@pytest.fixture(scope="class")
def login(sb):
    sb.open("https://www.saucedemo.com")
    sb.type("#user-name", "standard_user")
    sb.type("#password", "secret_sauce\n")


@pytest.fixture(scope="class")
def close_browser_after_test(sb):
    sb._reuse_session = False
