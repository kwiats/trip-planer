
## attractions
### /attractions/all -> get all atractions
request ->
```json

```
response ->
```json
[
  {
    "name": "string",
    "description": "string",
    "latitude": 0,
    "longitude": 0,
    "open_hours": {
      "additionalProp1": {
        "open": 0,
        "close": 0
      },
      "additionalProp2": {
        "open": 0,
        "close": 0
      },
      "additionalProp3": {
        "open": 0,
        "close": 0
      }
    },
    "category": "gastronomy",
    "address": "string",
    "city": "string",
    "country": "string",
    "media": [],
    "id": 0,
    "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "rating": 0,
    "time_spent": 0,
    "price": 0,
    "visits": 0
  }
]
```

### /attractions/create

request ->
```json
{
  "name": "Name of attraction",
  "description": "bla",
  "latitude": 12.4567,
  "longitude": 24.8909,
  "category": "gastronomy",
  "address": "dsfds",
  "city": "sfdds",
  "country": "sdfds",
  "media": [],
  "id": 0,
  "user_id": "b635d639-7fda-43c4-bc07-5a52b99c4146",
  "rating": 0,
  "time_spent": 0,
  "price": 0,
  "visits": 0
}
```
response -> this same

### /attractions/{id} -> get attraction by id

request -> path id
response -> one attraction

### /attractions/{id}/update -> update attraction by id

request -> path id
response -> one attraction

### /attractions/{id}/delete -> delete attraction by id

request -> path id
response -> deleted

### /attractions/{id}/images -> get image attraction by id

request -> path id
response ->
```json
{
  "id": 0,
  "image_urls": []
}
```

### /attractions/ -> filter by country, state, city, latitude, longitude, category, radius, sort_by, sort_direction

request ->
? costam ale 
sort_by
    TopRated = "topRated"
    MostRated = "mostRated"
sort_direction
    Asc = "asc"
    Desc = "desc"