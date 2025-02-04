from copy import copy

import pytest
from django.contrib.auth.hashers import check_password

from apps.users.models import Profile, User

@pytest.mark.django_db
def test_get_user_queryset(users_load):
    assert User.objects.get_queryset().count() == 3

@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"], indirect=True)
def test_get_user(user_db):
    print(user_db)
    user = User.objects.get_user(email=user_db.email)
    assert isinstance(user, User)

@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"], indirect=True)
def test_get_user_by_id(user_db):
    user = User.objects.get_user_by_id(user_id=user_db.id)
    assert isinstance(user, User)


@pytest.mark.django_db
def test_get_queryset_with_profile(profiles_load):
    assert User.objects.get_queryset_with_profile().count() == 2

@pytest.mark.django_db
@pytest.mark.parametrize(
    "email, password, username",
    [
        ("some_example1@example.com", "SomeSecurePassword12345!", "alibaba"),
        ("some_example2@example.com", "RandomPassword12345!", "cosmo"),
    ],
)
def test_create_user(email, password, username):
    user = User.objects.create_user(email=email, password=password, username=username)
    assert isinstance(user, User)
    assert check_password(password, user.password)
    assert user.is_active is False
    assert user.is_staff is False
    assert user.is_superuser is False
    assert hasattr(user, "profile") is False


@pytest.mark.django_db
@pytest.mark.parametrize(
    "email, password, username",
    [
        ("some_superuser_example1@example.com", "SomeSecurePassword12345!", "ann23432"),
        ("some_superuser_example2@example.com", "RandomPassword12345!", "rob1423"),
    ],
)
def test_create_superuser(email, password, username):
    user = User.objects.create_superuser(email=email, password=password, username=username)
    assert isinstance(user, User)
    assert check_password(password, user.password)
    assert user.is_active is False
    assert user.is_staff is True
    assert user.is_superuser is True
    assert hasattr(user, "profile") is False

@pytest.mark.django_db
@pytest.mark.parametrize(
    "new_email, new_password, new_username",
    [
        ("new@example.com", "NewPassword12345!", "new_username"),
    ],
)
@pytest.mark.parametrize("user_db", ["ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"], indirect=True)
def test_update_user(user_db, new_email, new_password, new_username):
    old_user = copy(user_db)
    updated_user = User.objects.update_user(
        user=user_db,
        email=new_email,
        password=new_password,
        username=new_username,
    )
    assert isinstance(updated_user, User)
    assert check_password(new_password, updated_user.password)
    assert updated_user.password != old_user.password
    assert updated_user.email != old_user.email
    assert updated_user.username != old_user.username


@pytest.mark.django_db
@pytest.mark.parametrize(
    "email, password, is_superuser",
    [
        ("new@example.com", "NewPassword12345!", False),
    ],
)
def test_create_superuser_without_superuser(email, password, is_superuser):
    with pytest.raises(ValueError, match="Superuser must have is_superuser=True."):
        User.objects.create_superuser(
            email=email, password=password, is_superuser=is_superuser
        )

@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"], indirect=True)
def test_delete_user(user_db):
    deleted_user = copy(user_db)
    User.objects.delete_user(user=user_db)
    with pytest.raises(User.DoesNotExist):
        User.objects.get(id=deleted_user.id)

# profile

@pytest.mark.django_db
def test_get_profile_queryset(profiles_load):
    assert Profile.objects.get_queryset().count() == 2

@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"], indirect=True)
def test_get_profile(profiles_load, user_db):
    profile = Profile.objects.get_profile(user=user_db)
    assert isinstance(profile, Profile)

@pytest.mark.django_db
@pytest.mark.parametrize("profile_db", [2], indirect=True)
def test_get_profile_by_id(profiles_load, profile_db):
    profile = Profile.objects.get_profile_by_id(profile_id=profile_db.id)
    assert isinstance(profile, Profile)

@pytest.mark.django_db
@pytest.mark.parametrize("user_db", ["6bc9da01-9f4c-4338-89da-019f4ca33858"], indirect=True)
def test_create_profile(user_db):
    profile = Profile.objects.create_profile(user=user_db)
    assert isinstance(profile, Profile)

@pytest.mark.django_db
@pytest.mark.parametrize("profile_db", [1], indirect=True)
def test_update_profile(profiles_load, profile_db):
    old_profile = copy(profile_db)
    new_data = {"first_name": "NewJohn", "last_name": "NewDoe"}
    new_profile = Profile.objects.update_profile(
        user=profile_db.user,
        profile=profile_db,
        first_name=new_data["first_name"],
        last_name=new_data["last_name"],
    )
    assert isinstance(new_profile, Profile)
    assert new_profile.first_name != old_profile.first_name
    assert new_profile.last_name != old_profile.last_name

@pytest.mark.django_db
@pytest.mark.parametrize("profile_db", [1], indirect=True)
def test_delete_profile(profiles_load,profile_db):
    deleted_profile = copy(profile_db)
    Profile.objects.delete_profile(profile=profile_db)
    with pytest.raises(Profile.DoesNotExist):
        Profile.objects.get(id=deleted_profile.id)