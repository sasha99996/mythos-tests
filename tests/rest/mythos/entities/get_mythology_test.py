import pytest
from clients.rest.base_http import send_request
from storage.urls import MythosUrls
from clients.rest.mythos_sandbox.entities import get_all_mythology, get_mythology_by_id
from clients.rest.base_validation import check_response_code, check_value_in_dicts, check_dicts_are_sorted_by_key



class TestMythology:
    def test_get_mythology_list(self):
        response = send_request("GET", MythosUrls.MYTHOLOGE_URL)
        assert response.status_code == 200


    @pytest.mark.parametrize("category", ["gods", "heroes", "creatures"])
    def test_get_mythology_list_with_category_filter(self, category):
        response = get_all_mythology(params={"category": category})
        check_response_code(response, expected_code=200)
        check_value_in_dicts(response.json(), key="category", value=category)


    @pytest.mark.parametrize("sort, reverse", [("asc", False), ("desc", True)])
    def test_get_mythology_list_with_category_filter_1(self, sort, reverse):
        response = get_all_mythology(params={"category": "creatures", "sort": sort})
        check_response_code(response, 200)
        check_dicts_are_sorted_by_key(response.json(), key="name", reverse=reverse)
