# Profiles

### GET /profiles

request -> z user id

response -> 
```JSON
{
  "name": "basic",
  "surname": "basic"
}
```

### UPDATE /profiles/update

request -> z user id
```JSON
{
  "name": "basic_new",
  "surname": "basic_new"
}
```
response -> z user id
```JSON
{
  "message": "Profile updated successfully"
}
```