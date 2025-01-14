# Authorizations

### GET /auth/register
request ->
```json
{
  "email": "basic@basic.com",
  "password": "Password123!",
  "profile": {
    "name": "basic",
    "surname": "basic"
  },
  "rewrite_password": "Password123!",
  "username": "basic"
}
```

response ->
```json
{
  "message": "User registered successfully"
}
```

### GET /auth/login

request ->
```json
{
  "password": "Password123!",
  "username": "basic"
}
```

response ->
```JSON
{
  "access_token": "test_token_access",
  "refresh_token": "test_token_refresh",
  "token_type": "Bearer"
}
```

### GET /auth/refresh
request ->
```JSON
{
  "refresh_token": "test_token_refresh"
}
```

response ->
```JSON
{
  "access_token": "test_token_access",
  "refresh_token": "test_token_refresh",
  "token_type": "Bearer"
}
```