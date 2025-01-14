# Users

### users/change-email

request ->
```JSON
{
  "new_email": "basic@basic.com",
  "old_email": "basic@basic.com",
  "password": "Password123!"
}
```

response ->
```JSON
{
  "message": "Password changed successfully"
}
```

### users/change-password

request ->
```JSON
{
  "new_password": "Password123!",
  "old_password": "basic@basic.com",
  "rewrite_password": "Password123!"
}
```

response ->
```JSON
{
  "message": "Password changed successfully"
}
```

### users/delete-account

request -> bierze zalogowanego usera id i wylogowuje go

response -> wraca na strone główna
```JSON
{
  "message": "User deleted successfully"
}
```