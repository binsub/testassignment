import logging

import pytest
from flask import url_for


@pytest.fixture(scope="module")
def test_client():
    app = create_app(Config)
    client = app.test_client()

    app_context = app.app_context()
    app_context.push()

    yield client

    app_context.pop()


def test_create_trip(test_client):
    request1 = test_client.post(
        "/api/v1/trip",
        json={
            "trip_code": "124",
            "payment": 13.30,
            "pick_up_location": "Strathfield",
            "drop_off_location": "Wynard",
            "driver_name": "Luxy",
            "customer_name": "Binaya",
            "car_number": "12345",
        },
    )
    assert request1.status_code == 201


# def test_id_from_abn(test_client):
#     request1 = test_client.get("/api/v1/trips?trip_abn=34534534534")
#     request2 = test_client.get("/api/v1/trips?trip_abn=34534")

#     assert request1.status_code == 200
#     assert request2.status_code == 404


def test_trip_exist(test_client):
    request1 = test_client.post(
        "/api/v1/trip",
        json={
            "trip_code": "124",
            "payment": 13.30,
            "pick_up_location": "Strathfield",
            "drop_off_location": "Wynard",
            "driver_name": "Luxy",
            "customer_name": "Binaya",
            "car_number": "12345",
        },
    )

    assert request1.status_code == 409


def test_get_trip(test_client):
    response = test_client.get("/api/v1/trip/124")

    assert response.status_code == 200


def test_edit_trip(test_client):
    response = test_client.put(
        "/api/v1/trip/2",
        json={
            {
                "trip_code": "changed",
                "payment": 13.30,
                "pick_up_location": "Strathfield",
                "drop_off_location": "Wynard",
                "driver_name": "Luxy",
                "customer_name": "Binaya",
                "car_number": "12345",
            }
        },
    )

    assert response.status_code == 204


def test_delete_trip(test_client):
    response = test_client.delete("/api/v1/trip/1")

    assert response.status_code == 204
