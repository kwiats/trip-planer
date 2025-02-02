import pytest
import boto3
from moto import mock_aws
from django.conf import settings
from apps.media.models import Media
from apps.media.services import MediaService, MediaS3Boto3Storage
from apps.media.enums import BucketNames, BucketNamesID
import uuid
import io
from io import BytesIO
from PIL import Image


@pytest.fixture(autouse=True)
def load_settings():
    settings.STORAGE_ACCESS_KEY = "fake_access_key"
    settings.STORAGE_SECRET_KEY = "fake_secret_key"
    settings.STORAGE_ENDPOINT_URL = "http://localstack:4566"
    settings.MEDIA_FILE_SIZE = 1000


@pytest.fixture
def s3_client():
    with mock_aws():
        client = boto3.client(
            service_name="s3",
            aws_access_key_id=settings.STORAGE_ACCESS_KEY,
            aws_secret_access_key=settings.STORAGE_SECRET_KEY,
            endpoint_url=settings.STORAGE_ENDPOINT_URL,
        )
        yield client

@pytest.fixture
def mock_storage(s3_client):
    storage = MediaS3Boto3Storage()
    storage.client = s3_client
    return storage

@pytest.fixture
def mock_media_service(mock_storage):
    media_service = MediaService(storage=mock_storage)
    return media_service

@pytest.fixture
def fake_image():
    in_memory_file = BytesIO()
    image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
    image.save(in_memory_file,'webp')
    in_memory_file.name = 'fake_name.webp'
    in_memory_file.seek(0)
    return in_memory_file
