import pytest
from app.main import fib


class TestFibUnit:
    def test_base_case_zero(self):
        assert fib(0) == 0

    def test_base_case_one(self):
        assert fib(1) == 1

    def test_second_term(self):
        assert fib(2) == 1

    def test_tenth_term(self):
        assert fib(10) == 55

    def test_upper_boundary(self):
        result = fib(500)
        assert isinstance(result, int)
        assert result > 0


class TestRootEndpoint:
    def test_returns_200(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_returns_message(self, client):
        response = client.get("/")
        assert "message" in response.json()


class TestFibonacciEndpoint:
    def test_n_zero(self, client):
        response = client.get("/fibonacci?n=0")
        assert response.status_code == 200
        assert response.json()["nth_term"] == 0

    def test_n_one(self, client):
        response = client.get("/fibonacci?n=1")
        assert response.status_code == 200
        assert response.json()["nth_term"] == 1

    def test_n_ten(self, client):
        response = client.get("/fibonacci?n=10")
        assert response.status_code == 200
        assert response.json()["nth_term"] == 55

    def test_upper_boundary(self, client):
        response = client.get("/fibonacci?n=500")
        assert response.status_code == 200
        assert response.json()["number"] == 500

    def test_negative_n_returns_400(self, client):
        response = client.get("/fibonacci?n=-1")
        assert response.status_code == 400

    def test_over_limit_returns_400(self, client):
        response = client.get("/fibonacci?n=501")
        assert response.status_code == 400

    def test_response_shape(self, client):
        response = client.get("/fibonacci?n=5")
        data = response.json()
        assert "message" in data
        assert "number" in data
        assert "nth_term" in data
