# threads

### POST /threads/create
request -> 
```JSON
{
  "attraction_id": 0,
  "rating": 0,
  "price": 0,
  "time_spent": 0,
  "title": "string",
  "description": "string"
}
```

### GET /threads/{review_id}

request ->
review_id uuid (required)

response ->
```JSON
{
  "attraction_id": 0,
  "rating": 0,
  "price": 0,
  "time_spent": 0,
  "title": "string",
  "description": "string",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "comments": [],
  "media": []
}
```

### DELETE /threads/{review_id}

request ->
review_id uuid (required)

response ->

### PATCH /threads/{review_id}

request ->
review_id uuid (required)
```JSON
{
  "attraction_id": 0,
  "rating": 0,
  "price": 0,
  "time_spent": 0,
  "title": "string",
  "description": "string"
}
```

response ->
```JSON
{
  "attraction_id": 0,
  "rating": 0,
  "price": 0,
  "time_spent": 0,
  "title": "string",
  "description": "string",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "comments": [],
  "media": []
}
```

### DELETE /threads/comment/{comment_id}

request ->
comment_id uuid (required)

response ->

### PATCH /threads/comment/{comment_id}

request ->
comment_id uuid (required)
```JSON
{
  "review_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "content": "string"
}
```

response ->
```JSON
{
  "review_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "content": "string",
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "created_at": "2025-01-12T18:35:16.633Z",
  "media": []
}
```

### GET /threads/attraction/{attraction_id}

request ->
attraction_id int (required)
sort_by string (optional)
rating int (optional)
price int (optional)
time_spent int (optional)

response ->
```JSON
[
  {
    "attraction_id": 0,
    "rating": 0,
    "price": 0,
    "time_spent": 0,
    "title": "string",
    "description": "string",
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "comments": [],
    "media": []
  }
]
```

### POST /threads/comment

request ->
```JSON
{
  "review_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "content": "string"
}
```

response ->
