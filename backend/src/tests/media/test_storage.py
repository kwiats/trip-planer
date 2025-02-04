import pytest
from apps.media.enums import BucketNames

@pytest.fixture
@pytest.mark.django_db
@pytest.mark.parametrize(
    "bucket_name", [
        BucketNames.USERS.value,
        BucketNames.COMMENTS.value,
        BucketNames.REVIEWS.value,
        BucketNames.ATTRACTIONS.value
    ]
)
def test_create_bucket(mock_storage, bucket_name):
    mock_storage.create_bucket(bucket_name=bucket_name, region_name="us-east-1")

    assert mock_storage.is_bucket_exists(bucket_name)


@pytest.mark.django_db
@pytest.mark.parametrize(
    "bucket_name", ["users"]
)
def test_delete_bucket(mock_storage, bucket_name):
    mock_storage.delete_bucket(bucket_name=bucket_name)

    assert not mock_storage.is_bucket_exists(bucket_name)


@pytest.mark.django_db
def test_upload_file(mock_storage, fake_image):
    bucket_name = 'test-bucket'
    file_name = 'test-file.webp'
    file_content = 'image/webp'
    file_size = len(fake_image.getvalue())
    file = fake_image

    mock_storage.create_bucket(bucket_name)

    mock_storage.upload_file(
        bucket_name=bucket_name,
        file_name=file_name,
        file=file,
        file_size=file_size,
        content_type=file_content
    )

    retrieved_file = mock_storage.retrieve_file(bucket_name, file_name)
    assert mock_storage.is_file_exists(bucket_name, file_name)
    assert mock_storage.get_file_size(bucket_name, file_name) == file_size
    assert mock_storage.get_file_type(bucket_name, file_name) == file_content
    assert mock_storage.get_file_name(bucket_name, file_name) == file_name
    assert mock_storage.get_file_url(bucket_name, file_name) == "http://localstack:4566/test-bucket/test-file.webp"
    assert retrieved_file == file.getvalue()

