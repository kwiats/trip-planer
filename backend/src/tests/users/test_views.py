import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"], indirect=True)
def test_user_detail_get_view(user_db):
    client = APIClient()
    client.force_authenticate(user=user_db)
    response = client.get(path=reverse("user-detail"))
    assert response.status_code == 200
    assert response.data["email"] == "test_user@example.com"

@pytest.mark.django_db
@pytest.mark.parametrize(
    "data", [{"username": "new_username", "first_name": "NewJohn", "last_name": "NewDoe"}]
)
@pytest.mark.parametrize("user_db", ["ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"], indirect=True)
def test_user_detail_put_view(profiles_load, user_db, data):
    client = APIClient()
    client.force_authenticate(user=user_db)
    response = client.put(
        path=reverse("user-detail"),
        data=data,
        format="json",
    )
    assert response.status_code == 200
    assert response.data == {
        "username": "new_username",
        "email": "test_user@example.com",
        "profile": {"full_name": "NewJohn NewDoe"},
    }


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"], indirect=True)
def test_user_detail_patch_view(profiles_load, user_db):
    client = APIClient()
    client.force_authenticate(user=user_db)
    new_user_data = {
        "first_name": "NewJohn",
    }
    response = client.patch(
        path=reverse("user-detail"),
        data=new_user_data,
        format="json",
    )
    assert response.status_code == 200
    assert response.data == {
        "username": "test_user",
        "email": "test_user@example.com",
        "profile": {"full_name": ""},
    }


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"], indirect=True)
def test_user_detail_delete_view(user_db):
    client = APIClient()
    client.force_authenticate(user=user_db)
    response = client.delete(path=reverse("user-detail"))
    assert response.status_code == 204

@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["6bc9da01-9f4c-4338-89da-019f4ca33858"], indirect=True)
def test_user_create_view(users_load, user_db):
    client = APIClient()
    client.force_authenticate(user=user_db)

    new_profile_data = {
        "first_name": "Alan",
        "last_name": "Smith",
    }
    response = client.post(
        path=reverse("user-create"),
        data=new_profile_data,
        format="json",
    )

    assert response.status_code == 201
    assert response.data == {
        "username": "admin",
        "email": "admin@example.com",
        "profile": {"full_name": "Alan Smith"},
    }


@pytest.mark.django_db
@pytest.mark.parametrize(
    "data", [{
        "new_email": "example@example.com",
        "old_email": "test_user@example.com",
        "password": "RandomPassword12345!",
        "rewrite_password": "RandomPassword12345!",
    }]
)
@pytest.mark.parametrize("user_db", ["ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"], indirect=True)
def test_change_email_view(user_db, data):
    client = APIClient()
    client.force_authenticate(user=user_db)
    response = client.put(
        path=reverse("change-email"),
        data=data,
        format="json",
    )
    assert response.status_code == 200
    assert response.data == {"detail": "Email changed successfully"}


@pytest.mark.django_db
@pytest.mark.parametrize(
    "data", [{
        "old_password": "RandomPassword12345!",
        "new_password": "examplePassword1234",
        "rewrite_new_password": "examplePassword1234",
    }]
)
@pytest.mark.parametrize("user_db", ["ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"], indirect=True)
def test_change_password_view(user_db, data):
    client = APIClient()
    client.force_authenticate(user=user_db)
    response = client.put(
        path=reverse("change-password"),
        data=data,
        format="json",
    )
    assert response.status_code == 200
    assert response.data == {"detail": "Password changed successfully"}


@pytest.mark.django_db
@pytest.mark.parametrize(
    "data", [{
        "old_password": "RandomPassword12345!",
        "new_password": "RandomPassword12345!",
        "rewrite_new_password": "RandomPassword12345!",
    }]
)
@pytest.mark.parametrize("user_db", ["ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"], indirect=True)
def test_change_password_invalid_view(user_db, data):
    client = APIClient()
    client.force_authenticate(user=user_db)
    response = client.put(
        path=reverse("change-password"),
        data=data,
        format="json",
    )
    assert response.status_code == 400
    assert str(response.data["errors"][0]) == "New password can't be the same as the old one"