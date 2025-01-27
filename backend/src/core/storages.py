import io
import json
import logging
from typing import BinaryIO

import boto3
from botocore.exceptions import ClientError
from django.conf import settings

from apps.media.enums import BucketNames


class MediaS3Boto3Storage:
    def __init__(
        self,
        access_key: str = None,
        secret_key: str = None,
        endpoint_url: str = None,
        **kwargs,
    ):
        self.access_key = access_key or settings.STORAGE_ACCESS_KEY
        self.secret_key = secret_key or settings.STORAGE_SECRET_KEY
        self.endpoint_url = endpoint_url or settings.STORAGE_ENDPOINT_URL
        self.default_acl = kwargs.pop("default_acl", "public-read")

        self.session = boto3.Session(
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
        )

        self.client = self.session.client(
            service_name="s3",
            endpoint_url=self.endpoint_url,
            **kwargs,
        )

        self.set_default_buckets()

    def set_default_buckets(self) -> str:  # noqa
        for bucket_name in BucketNames:
            self.create_bucket(bucket_name.value)
            self.set_bucket_policy(bucket_name.value)

    def set_bucket_policy(self, bucket_name: str) -> None:
        bucket_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "PublicReadGetObject",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": f"arn:aws:s3:::{bucket_name}/*",
                }
            ],
        }

        self.client.put_bucket_policy(
            Bucket=bucket_name, Policy=json.dumps(bucket_policy)
        )

    def create_bucket(self, bucket_name: str, region_name: str = None):
        if self.is_bucket_exists(bucket_name):
            pass
        else:
            if any(host in self.endpoint_url for host in settings.ALLOWED_HOSTS):
                self.client.create_bucket(Bucket=bucket_name)
            else:
                self.client.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={"LocationConstraint": region_name},
                )

    def is_bucket_exists(self, bucket_name: str) -> bool:
        try:
            self.client.head_bucket(Bucket=bucket_name)
            return True
        except ClientError as error:
            if error.response["Error"]["Code"] == "404":
                return False

    def delete_bucket(self, bucket_name: str) -> None:
        try:
            self.client.delete_bucket(Bucket=bucket_name)
            logging.info(f"Bucket {bucket_name} deleted successfully.")
        except Exception as error:
            logging.error(f"Error deleting bucket {bucket_name}: {error}")

    def upload_file(
        self,
        bucket_name: str,
        file_name: str,
        file: BinaryIO,
        file_size: int,
        content_type: str,
        **kwargs,
    ):
        if not self.is_bucket_exists(bucket_name):
            raise ValueError(f"Bucket {bucket_name} does not exist.")

        try:
            self.client.put_object(
                Bucket=bucket_name,
                Key=file_name,
                Body=file,
                ContentLength=file_size,
                ContentType=content_type,
                ACL=self.default_acl,
                **kwargs,
            )
        except ClientError as error:
            logging.error(
                f"Error uploading file {file_name} to bucket {bucket_name}: {error.response['Error']['Message']}"
            )
            raise ValueError(
                f"Error uploading file {file_name} to bucket {bucket_name}: {error.response['Error']['Message']}"
            )

        logging.info(f"File {file_name} uploaded to bucket {bucket_name} successfully.")

    def retrieve_file(self, bucket_name: str, filename: str) -> bytes:
        if not self.is_bucket_exists(bucket_name):
            raise ValueError(f"Bucket {bucket_name} does not exist.")

        try:
            response = self.client.get_object(Bucket=bucket_name, Key=filename)
            with response:
                data_stream = io.BytesIO(response.data)
                data = data_stream.read()
            return data
        except ClientError as error:
            logging.error(
                f"Error retrieving file {filename} from bucket {bucket_name}: {error.response['Error']['Message']}"
            )
            raise ValueError(
                f"Error retrieving file {filename} from bucket {bucket_name}: {error.response['Error']['Message']}"
            )

    def delete_file(self, bucket_name: str, filename: str) -> None:
        if not self.is_bucket_exists(bucket_name):
            raise ValueError(f"Bucket {bucket_name} does not exist.")

        try:
            self.client.delete_object(Bucket=bucket_name, Key=filename)
            logging.info(
                f"File {filename} deleted from bucket {bucket_name} successfully."
            )
        except ClientError as error:
            logging.error(
                f"Error deleting file {filename} from bucket {bucket_name}: {error.response['Error']['Message']}"
            )
            raise ValueError(
                f"Error deleting file {filename} from bucket {bucket_name}: {error.response['Error']['Message']}"
            )

        logging.info(f"File {filename} deleted from bucket {bucket_name} successfully.")

    def list_files(self, bucket_name: str) -> list[str]:
        if not self.is_bucket_exists(bucket_name):
            raise ValueError(f"Bucket {bucket_name} does not exist.")

        try:
            objects = self.client.list_objects(Bucket=bucket_name)
            return [obj["Key"] for obj in objects.get("Contents", [])]
        except ClientError as error:
            logging.error(
                f"Error listing files in bucket {bucket_name}: {error.response['Error']['Message']}"
            )
            raise ValueError(
                f"Error listing files in bucket {bucket_name}: {error.response['Error']['Message']}"
            )

    def get_file_url(self, bucket_name: str, filename: str) -> str:
        if not self.is_bucket_exists(bucket_name):
            raise ValueError(f"Bucket {bucket_name} does not exist.")

        url_link = f"{self.endpoint_url}/{bucket_name}/{filename}"

        return url_link
