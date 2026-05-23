import pytest
from clients.rest.base_http import send_request
from storage.urls import MythosUrls


class TestMythology:
    def test_get_mythology_id(self):
        response = send_request("GET", "https://api.qasandbox.ru/api/mythology/5")
        assert response.status_code == 200, "Сущность не найдена"
