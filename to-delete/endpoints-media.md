# media

### POST /media/create

request -> create media

file string(binary) required
attraction_id (can be null)
review_id (can be null)
comment_id (can be null)

### GET /media/{media_id}

request -> get media
media_id (string) required

response -> get media
```JSON
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "bucket_name": "string",
    "file_name": "string",
    "file_type": "string",
    "attraction_id": 0,
    "review_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "comment_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "created_at": "2025-01-12T18:22:24.431Z",
    "updated_at": "2025-01-12T18:22:24.431Z"
  }
]
```

### GET /media/by-attraction/{attraction_id}

request -> get media by attraction
attraction_id (string) required

response -> get media by attraction
```JSON
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "bucket_name": "string",
    "file_name": "string",
    "file_type": "string",
    "attraction_id": 0,
    "review_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "comment_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "created_at": "2025-01-12T18:22:24.431Z",
    "updated_at": "2025-01-12T18:22:24.431Z"
  }
]
```

### GET /media/by-comment/{comment_id}

request -> get media by comment
comment_id (string) required

response -> get media by comment
```JSON
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "bucket_name": "string",
    "file_name": "string",
    "file_type": "string",
    "attraction_id": 0,
    "review_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "comment_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "created_at": "2025-01-12T18:22:24.431Z",
    "updated_at": "2025-01-12T18:22:24.431Z"
  }
]
```

### GET /media/by-review/{review_id}

request -> get media by review
review_id (string) required

response -> get media by review
```JSON
[
  {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "bucket_name": "string",
    "file_name": "string",
    "file_type": "string",
    "attraction_id": 0,
    "review_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "comment_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "created_at": "2025-01-12T18:22:24.431Z",
    "updated_at": "2025-01-12T18:22:24.431Z"
  }
]
```

### UPDATE /media/{media_id}/update

request -> update media
media_id (string) required
```JSON
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "bucket_name": "string",
  "file_name": "string",
  "file_type": "string",
  "attraction_id": 0,
  "review_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "comment_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "updated_at": "2025-01-12T17:37:09.148128"
}
```

response -> update media
```JSON
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "bucket_name": "string",
  "file_name": "string",
  "file_type": "string",
  "attraction_id": 0,
  "review_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "comment_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "created_at": "2025-01-12T18:26:20.770Z",
  "updated_at": "2025-01-12T18:26:20.770Z"
}
```

### DELETE /media/{media_id}/delete

request -> delete media
media_id (string) required

response -> delete media

### GET /media/{bucket_name}/{object_id}/{filename}

request -> get media from cloud storage
bucket_name (string) required
object_id (string) required
filename (string) required

response -> get media from cloud storage

### GET /media/{bucket_name}/{filename}

request -> get default media from cloud storage
bucket_name (string) required
filename (string) required