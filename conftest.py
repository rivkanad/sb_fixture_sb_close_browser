import pytest

"""Overriding the "sb" fixture to make it class scoped."""


@pytest.fixture(scope="class")
def sb(request):

    from seleniumbase import BaseCase

    class BaseClass(BaseCase):
        def setUp(self):
            super(BaseClass, self).setUp()

        def tearDown(self):
            super(BaseClass, self).tearDown()

        def base_method(self):
            pass

        def open(self, url):
            super().open(url)

    if request.cls:
        request.cls.sb = BaseClass("base_method")
        request.cls.sb.setUp()
        yield request.cls.sb
        request.cls.sb.tearDown()
    else:
        sb = BaseClass("base_method")
        sb.setUp()
        yield sb
        sb.tearDown()


@pytest.fixture()
def login(sb):
    if not (is_logged_in := sb.is_element_visible("#react-burger-menu-btn")):
        sb.open("https://www.saucedemo.com")
        sb.type("#user-name", "standard_user")
        sb.type("#password", "secret_sauce\n")


@pytest.fixture(scope="class", autouse=True)
def close_browser(sb):
    yield
    sb._reuse_session = False
