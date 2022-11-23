import pytest
import logging
LOGGER = logging.getLogger(__name__)
"""Overriding the "sb" fixture to make it class scoped."""


# @pytest.fixture()
# def sb(request):
#
#     from seleniumbase import BaseCase
#
#     class BaseClass(BaseCase):
#         def setUp(self):
#             super(BaseClass, self).setUp()
#
#         def tearDown(self):
#             self.save_teardown_screenshot()
#             super(BaseClass, self).tearDown()
#
#         def base_method(self):
#             pass
#
#         def open(self, url):
#             super().open(url)
#
#     if request.cls:
#         request.cls.sb = BaseClass("base_method")
#         request.cls.sb.setUp()
#
#         # request.cls.sb._needs_tearDown = True
#
#         yield request.cls.sb
#         request.cls.sb.tearDown()
#     else:
#         sb = BaseClass("base_method")
#         sb.setUp()
#         yield sb
#         sb.tearDown()


@pytest.fixture()
def login(sb, request):
    print("current page is " + sb.get_current_url())
    if not (is_logged_in := sb.is_element_visible("#react-burger-menu-btn")):
        sb.open("https://www.saucedemo.com")
        sb.type("#user-name", "standard_user")
        sb.type("#password", "secret_sauce\n")


@pytest.fixture(autouse=True)
def close_browser(sb, request):
    if request.cls.last_func == request.node.name:
        request.cls.sb._reuse_session = False
    yield

# conftest.py
def pytest_collection_modifyitems(items):
    """sets attribute for each class that saves the name of the last and first functions in the class"""
    last_class_function = {item.cls: item.name for item in items}
    first_class_function_mapping = {item.cls: item.name for item in reversed(items)}

    for test_cls in last_class_function:
        # set name of last function for each class
        test_cls.last_func = last_class_function[test_cls]

    for test_cls in first_class_function_mapping:
        # set name of first function for each class
        test_cls.first_func = first_class_function_mapping[test_cls]
