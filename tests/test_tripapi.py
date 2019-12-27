def test_create_trip(client):
    request1 = client.post(
        "/api/v1/trip",
        json={
            "trip_code": "1243",
            "payment": 13.30,
            "pick_up_location": "Strathfield",
            "drop_off_location": "Wynard",
            "driver_name": "Luxy",
            "customer_name": "Binaya",
            "car_number": "12345",
        },
    )
    assert request1.status_code == 201


def test_id_from_trip_code(client):
    request1 = client.get("/api/v1/trips?trip_code=1243")
    assert request1.status_code == 200


# def test_trip_exist(test_client):
#     request1 = test_client.post(
#         "/api/v1/trip",
#         json={
#             "trip_code": "124",
#             "payment": 13.30,
#             "pick_up_location": "Strathfield",
#             "drop_off_location": "Wynard",
#             "driver_name": "Luxy",
#             "customer_name": "Binaya",
#             "car_number": "12345",
#         },
#     )

#     assert request1.status_code == 409


# def test_get_trip(test_client):
#     response = test_client.get("/api/v1/trip/124")

#     assert response.status_code == 200


# def test_edit_trip(test_client):
#     response = test_client.put(
#         "/api/v1/trip/2",
#         json={
#             {
#                 "trip_code": "changed",
#                 "payment": 13.30,
#                 "pick_up_location": "Strathfield",
#                 "drop_off_location": "Wynard",
#                 "driver_name": "Luxy",
#                 "customer_name": "Binaya",
#                 "car_number": "12345",
#             }
#         },
#     )

#     assert response.status_code == 204


# def test_delete_trip(test_client):
#     response = test_client.delete("/api/v1/trip/1")

#     assert response.status_code == 204
