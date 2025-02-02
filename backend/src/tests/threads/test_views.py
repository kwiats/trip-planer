import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"], indirect=True)
@pytest.mark.parametrize("attraction_db", [1], indirect=True)
def test_review_create_view(attractions_load, attraction_db, user_db):
    client = APIClient()
    client.force_authenticate(user=user_db)


    review_data = {
        "rating": 5,
        "price": "1258.00",
        "time_spent": "03:20:00",
        "title": "string",
        "description": "string",
        "attraction_id": attraction_db.id,
    }

    response = client.post(
        path=reverse("review-create"),
        data=review_data,
        format="json",
    )
    assert response.status_code == 201
    for field in ["id", "media", "comments"]:
        response.data.pop(field)
    assert response.data == review_data


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"], indirect=True)
@pytest.mark.parametrize("review_db", ["eed922f1-ed5d-4494-9922-f1ed5d44949c"], indirect=True)
def test_review_detail_get_view(attractions_load, reviews_load, user_db, review_db):
    client = APIClient()
    client.force_authenticate(user=user_db)
    response = client.get(
        path=reverse(
            viewname="review-detail",
            kwargs={"id": review_db.id},
        ),
        format="json"
    )
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"], indirect=True)
@pytest.mark.parametrize("review_db", ["eed922f1-ed5d-4494-9922-f1ed5d44949c"], indirect=True)
@pytest.mark.parametrize("attraction_db", [1], indirect=True)
def test_review_update_put_view(attractions_load, reviews_load, user_db, attraction_db, review_db):
    client = APIClient()
    client.force_authenticate(user=user_db)

    review_data_update = {
        "rating": 3,
        "price": "699.73",
        "time_spent": "02:00:00",
        "title": "string",
        "description": "string",
        "attraction_id": attraction_db.id,
    }

    response = client.put(
        path=reverse(
            viewname="review-detail",
            kwargs={"id": review_db.id},
        ),
        data=review_data_update,
        format="json"
    )
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"], indirect=True)
@pytest.mark.parametrize("review_db", ["eed922f1-ed5d-4494-9922-f1ed5d44949c"], indirect=True)
@pytest.mark.parametrize("attraction_db", [1], indirect=True)
def test_review_update_patch_view(attractions_load, reviews_load, user_db, attraction_db, review_db):
    client = APIClient()
    client.force_authenticate(user=user_db)

    review_data_update = {
        "rating": 4,
    }

    response = client.patch(
        path=reverse(
            viewname="review-detail",
            kwargs={"id": review_db.id},
        ),
        data=review_data_update,
        format="json"
    )
    assert response.status_code == 200
    assert response.data["rating"] == 4


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"], indirect=True)
@pytest.mark.parametrize("review_db", ["eed922f1-ed5d-4494-9922-f1ed5d44949c"], indirect=True)
def test_review_delete_view(attractions_load, reviews_load, user_db, review_db):
    client = APIClient()
    client.force_authenticate(user=user_db)

    response = client.delete(
        path=reverse(
            viewname="review-detail",
            kwargs={"id": review_db.id},
        ),
        format="json"
    )
    assert response.status_code == 204


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"], indirect=True)
@pytest.mark.parametrize("review_db", ["eed922f1-ed5d-4494-9922-f1ed5d44949c"], indirect=True)
def test_comment_create_view(attractions_load, reviews_load, review_db, user_db):
    client = APIClient()
    client.force_authenticate(user=user_db)

    comment_data = {
        "content": "string",
        "review_id": review_db.id,
    }

    response = client.post(
        path=reverse("comment-create"),
        data=comment_data,
        format="json",
    )
    assert response.status_code == 201
    assert response.data["user_id"] == str(user_db.id)
    assert response.data["review_id"] == str(review_db.id)
    assert response.data["content"] == comment_data["content"]


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"], indirect=True)
@pytest.mark.parametrize("comment_db", ["1520fda8-f043-4163-a0fd-a8f043c16359"], indirect=True)
def test_comment_detail_get_view(attractions_load, reviews_load, comments_load, user_db, comment_db):
    client = APIClient()
    client.force_authenticate(user=user_db)
    response = client.get(
        path=reverse(
            viewname="comment-detail",
            kwargs={"id": comment_db.id},
        ),
        format="json"
    )
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"], indirect=True)
@pytest.mark.parametrize("comment_db", ["b1135911-4fcc-4a08-9359-114fcc0a0893"], indirect=True)
@pytest.mark.parametrize("review_db", ["eed922f1-ed5d-4494-9922-f1ed5d44949c"], indirect=True)
def test_comment_update_put_view(attractions_load, reviews_load, comments_load, user_db, comment_db, review_db):
    client = APIClient()
    client.force_authenticate(user=user_db)

    comment_data_update = {
        "content": "string",
        "review_id": review_db.id,
    }

    response = client.put(
        path=reverse(
            viewname="comment-detail",
            kwargs={"id": comment_db.id},
        ),
        data=comment_data_update,
        format="json"
    )
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"], indirect=True)
@pytest.mark.parametrize("comment_db", ["1520fda8-f043-4163-a0fd-a8f043c16359"], indirect=True)
def test_comment_update_patch_view(attractions_load, reviews_load, comments_load, user_db, comment_db):
    client = APIClient()
    client.force_authenticate(user=user_db)

    comment_data_update = {
        "content": "string",
        "review_id": comment_db.review_id,
    }

    response = client.patch(
        path=reverse(
            viewname="comment-detail",
            kwargs={"id": comment_db.id},
        ),
        data=comment_data_update,
        format="json"
    )
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"], indirect=True)
@pytest.mark.parametrize("comment_db", ["1520fda8-f043-4163-a0fd-a8f043c16359"], indirect=True)
def test_comment_delete_view(attractions_load, reviews_load, comments_load, user_db, comment_db):
    client = APIClient()
    client.force_authenticate(user=user_db)

    response = client.delete(
        path=reverse(
            viewname="comment-detail",
            kwargs={"id": comment_db.id},
        ),
        format="json"
    )
    assert response.status_code == 204
