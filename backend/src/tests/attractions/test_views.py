from uuid import UUID

import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"], indirect=True)
@pytest.mark.parametrize("attraction_db", [1], indirect=True)
def test_attraction_detail_view(attractions_load, attraction_db, user_db):
    client = APIClient()
    client.force_authenticate(user=user_db)
    response = client.get(
        path=reverse(
            viewname="attraction-detail",
            kwargs={"id": attraction_db.id},
        ),
        format="json",
    )
    assert response.status_code == 200
    expected_data = {
        "id": 1,
        "name": "Chick-fil-A",
        "description": "Some text",
        "longitude": -79.4132781,
        "latitude": 43.6428802,
        "open_hours": {
            "friday": ["08:00", "17:00"],
            "monday": ["08:00", "17:00"],
            "sunday": ["08:00", "17:00"],
            "tuesday": ["08:00", "17:00"],
            "saturday": ["08:00", "17:00"],
            "thursday": ["08:00", "17:00"],
            "wednesday": ["08:00", "17:00"],
        },
        "address": "709 Yonge St, Toronto",
        "city": "New York",
        "country": "USA",
        "rating": 0,
        "time_spent": 0,
        "price": 0,
        "visits": 0,
        "user_id": UUID("8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"),
        "categories": ["Museum", "Library"],
    }
    assert response.data == expected_data

@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"], indirect=True)
def test_attraction_list_view(attractions_load, user_db):
    client = APIClient()
    client.force_authenticate(user=user_db)
    response = client.get(path=reverse("attraction-list"), format="json")
    assert response.status_code == 200

@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"], indirect=True)
def test_attraction_create_view(user_db):
    client = APIClient()
    client.force_authenticate(user=user_db)
    new_attraction_data = {
        "name": "Foo Company",
        "description": "Some text",
        "longitude": -80.4132781,
        "latitude": 44.6428802,
        "open_hours": {
            "thursday": ["08:00", "17:00"],
            "wednesday": ["08:00", "17:00"],
        },
        "address": "Foo St, Toronto 34",
        "city": "Old York",
        "country": "USA",
        "add_categories": ["Restaurant"],
    }
    response = client.post(
        path=reverse("attraction-create"),
        data=new_attraction_data,
        format="json",
    )

    for field in ["price", "time_spent", "visits", "rating", "user_id", "id"]:
        response.data.pop(field)

    categories = response.data.pop("categories")

    assert categories == new_attraction_data.pop("add_categories")
    assert response.status_code == 201
    assert response.data == new_attraction_data


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"], indirect=True)
@pytest.mark.parametrize("attraction_db", [4], indirect=True)
def test_attraction_update_put_view(attractions_load, user_db, attraction_db):
    client = APIClient()
    client.force_authenticate(user=user_db)
    update_put_attraction_data = {
        "name": "New Foo Company Name",
        "description": "Some new text",
        "longitude": -80.4132781,
        "latitude": 44.6428802,
        "open_hours": {
            "thursday": ["08:00", "19:00"],
            "wednesday": ["08:00", "19:00"],
        },
        "address": "Foo St, Toronto 34",
        "city": "Old York",
        "country": "USA",
        "add_categories": ["Market"],
    }

    response = client.put(
        path=reverse(
            viewname="attraction-update",
            kwargs={"id": attraction_db.id},
        ),
        data=update_put_attraction_data,
        format="json",
    )
    for field in ["price", "time_spent", "visits", "rating", "user_id"]:
        response.data.pop(field)

    attraction_id = response.data.pop("id")
    categories = response.data.pop("categories")

    assert attraction_id == 4
    assert categories == update_put_attraction_data.pop("add_categories")
    assert response.status_code == 200
    assert response.data == update_put_attraction_data


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"], indirect=True)
@pytest.mark.parametrize("attraction_db", [4], indirect=True)
def test_attraction_update_patch_view(attractions_load, user_db, attraction_db):
    client = APIClient()
    client.force_authenticate(user=user_db)
    update_patch_attraction_data = {
        "name": "Kebab House",
        "open_hours": {
            "thursday": ["08:00", "17:00"],
            "wednesday": ["08:00", "17:00"],
        },
        "add_categories": ["Market"],
    }

    response = client.patch(
        path=reverse(
            viewname="attraction-update",
            kwargs={"id": attraction_db.id},
        ),
        data=update_patch_attraction_data,
        format="json",
    )
    assert response.status_code == 200
    assert response.data["name"] == update_patch_attraction_data["name"]
    assert response.data["open_hours"] == update_patch_attraction_data["open_hours"]
    assert response.data["categories"] == update_patch_attraction_data["add_categories"]


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"], indirect=True)
@pytest.mark.parametrize("attraction_db", [4], indirect=True)
def test_attraction_delete_view(attractions_load, attraction_db, user_db):
    client = APIClient()
    client.force_authenticate(user=user_db)
    response = client.delete(
        path=reverse(
            viewname="attraction-delete",
            kwargs={"id": attraction_db.id},
        ),
        format="json",
    )
    assert response.status_code == 204


@pytest.mark.parametrize("user_db", ["8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"], indirect=True)
@pytest.mark.parametrize("attraction_db", [1], indirect=True)
@pytest.mark.django_db
def test_attraction_images_view(attractions_load, reviews_load, comments_load, media_load, attraction_db, user_db):
    client = APIClient()
    client.force_authenticate(user=user_db)
    response = client.get(
        path=reverse(
            viewname="attraction-images",
            kwargs={"id": attraction_db.id},
        ),
        format="json",
    )
    assert response.status_code == 200
    assert response.data == {
        'id': 1,
        'images_urls': [
            'https://rar_image/rar_image.jpg',
            'https://some_image/some_image.jpg',
        ]
    }