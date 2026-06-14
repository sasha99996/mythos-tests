from clients.rest.mythos_sandbox.entities import register_user
from clients.data_generator import get_random_string
from clients.rest.base_validation import check_response_code


def test_register_success():
    new_user = get_random_string(size=6, string_type="letters")
    new_password = get_random_string(size=6, string_type="letters")
    new_us = register_user(username=new_user, password=new_password)
    check_response_code(new_us, 201)


