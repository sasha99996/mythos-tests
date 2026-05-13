import pytest
from clients.rest.base_http import send_request
from storage.urls import MythosUrls



class TestMythology:
    def test_get_mythology_list(self):
        response = send_request("GET", MythosUrls)
        assert response.status_code == 200
