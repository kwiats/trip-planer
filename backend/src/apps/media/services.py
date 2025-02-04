import logging
import uuid
from typing import Optional

from django.conf import settings

from apps.attractions.models import Attraction
from apps.media.enums import BucketNames, BucketNamesID
from apps.media.models import Media
from apps.media.utils import (
    create_file_name,
    prepare_file,
)
from core.storages import MediaS3Boto3Storage


class MediaService:
    def __init__(
        self,
        storage: "MediaS3Boto3Storage",
    ):
        self.storage = storage

    @staticmethod
    def _get_bucket_name(validated_data: dict[str, any]) -> str:
        mapping = {
            "attraction_id": BucketNames.ATTRACTIONS.value,
            "comment_id": BucketNames.COMMENTS.value,
            "review_id": BucketNames.REVIEWS.value,
        }

        for key, bucket_name in mapping.items():
            if validated_data.get(key):
                return bucket_name

        return validated_data.get("bucket_name")

    @staticmethod
    def _get_folder_name(validated_data: dict[str, any]) -> str:
        for key in BucketNamesID:
            folder_name = validated_data.get(key.value, None)
            if folder_name:
                if hasattr(folder_name, 'id'):
                    return str(folder_name.id)
                return str(folder_name)
        return str(validated_data.get("id"))

    def _create_file_name(self, validated_data: dict[str, any]) -> str:
        file_name = validated_data["file_name"]
        folder_name = self._get_folder_name(validated_data)
        return create_file_name(file_name=file_name, folder_name=folder_name)

    def create_media(self, validated_data: dict[str, any]) -> "Media":
        validated_data["id"] = str(uuid.uuid4())
        media_id = validated_data["id"]

        try:
            file_io, file_size, file_type = prepare_file(
                validated_data.pop("file"), validated_data.get("file_type")
            )
            bucket_name = self._get_bucket_name(validated_data)
            file_name = self._create_file_name(validated_data)
            if file_size > settings.MEDIA_FILE_SIZE:
                raise ValueError("File size is too large.")

            attraction = validated_data.pop("attraction_id", None)
            review = validated_data.pop("review_id", None)
            comment = validated_data.pop("comment_id", None)

            if not self.storage.is_bucket_exists(bucket_name):
                self.storage.create_bucket(bucket_name)

            # Upload file
            self.storage.upload_file(
                bucket_name=bucket_name,
                file_name=file_name,
                file=file_io,
                content_type=file_type,
                file_size=file_size,
            )
            # Create media object
            media = Media.objects.create_media(
                media_id=media_id,
                bucket_name=bucket_name,
                file_name=validated_data["file_name"],
                file_url=self.storage.get_file_url(bucket_name, file_name),
                file_type=file_type,
                attraction=attraction,
                review=review,
                comment=comment,
            )
            media.save()

            return media

        except Exception as error:
            logging.error(error)
            raise ValueError(error)

    @staticmethod
    def get_folder_name(media: "Media") -> Optional[str]:
        for attribute in [k.value for k in BucketNamesID]:
            if getattr(media, attribute):
                return str(getattr(media, attribute))

        return str(media.id)

    @staticmethod
    def get_media(media_id: str) -> "Media":
        return Media.objects.get(id=media_id)

    def delete_media(self, media: "Media") -> None:
        filename = f"{self.get_folder_name(media)}/{media.file_name}"
        self.storage.delete_file(media.bucket_name, filename)
        media.delete()
