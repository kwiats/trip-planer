import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.media.models import Media
from apps.media.services import MediaService
from apps.media.enums import BucketNames
from core.storages import MediaS3Boto3Storage



@pytest.fixture
def fake_file(fake_image):
    return SimpleUploadedFile("test-file.webp", fake_image.getvalue(), content_type="image/webp")


@pytest.fixture
@pytest.mark.django_db
@pytest.mark.parametrize("attraction_db", [1], indirect=True)
def test_create_media(attractions_load, attraction_db, mock_media_service, mock_storage, fake_file):
    validated_data = {
        "bucket_name": BucketNames.ATTRACTIONS.value,
        "file": fake_file,
        "file_name": "test-file.webp",
        "file_type": "image/webp",
        "attraction_id": attraction_db,
        "review_id": None,
        "comment_id": None
    }

    media = mock_media_service.create_media(validated_data)

    assert mock_storage.is_bucket_exists(BucketNames.ATTRACTIONS.value)
    assert Media.objects.filter(id=media.id).exists()
    assert mock_storage.get_file_name(BucketNames.ATTRACTIONS.value, "test-file.webp") \
           == Media.objects.get(id=media.id).file_name
    assert mock_storage.get_file_url(BucketNames.ATTRACTIONS.value, "1/test-file.webp") \
           == Media.objects.get(id=media.id).file_url


@pytest.mark.django_db
@pytest.mark.parametrize("media_db", ["ad1329d9-e1a9-429e-9329-d9e1a9129ede"], indirect=True)
def test_get_folder_name(
        attractions_load,
        reviews_load,
        comments_load,
        media_load,
        media_db,
        mock_media_service,
):
    folder_name = mock_media_service.get_folder_name(media_db)

    assert folder_name


@pytest.mark.django_db
@pytest.mark.parametrize("media_db", ["ad1329d9-e1a9-429e-9329-d9e1a9129ede"], indirect=True)
def test_get_media(
        attractions_load,
        reviews_load,
        comments_load,
        media_load,
        media_db,
        mock_media_service,
):
    media = mock_media_service.get_media(media_id=media_db.id)

    assert media.file_url == "https://some_image/some_image.jpg"
    assert isinstance(media, Media)

@pytest.mark.django_db
@pytest.mark.parametrize("attraction_db", [1], indirect=True)
def test_delete_media(
        attractions_load,
        reviews_load,
        comments_load,
        mock_storage,
        mock_media_service,
        fake_file,
        attraction_db,
):
    validated_data = {
        "bucket_name": BucketNames.ATTRACTIONS.value,
        "file": fake_file,
        "file_name": "test-file.webp",
        "file_type": "image/webp",
        "attraction_id": attraction_db,
        "review_id": None,
        "comment_id": None
    }

    media = mock_media_service.create_media(validated_data)
    filename = f"{media.attraction.id}/{media.file_name}"
    mock_storage.get_file_url(media.bucket_name, filename)
    mock_storage.is_file_exists(media.bucket_name, filename)


    mock_media_service.delete_media(media=media)
    assert not Media.objects.filter(id=media.id).exists()
    assert not mock_storage.is_file_exists(media.bucket_name, filename)
    with pytest.raises(Media.DoesNotExist):
        Media.objects.get(id=media.id)