import pytest


@pytest.fixture(autouse=True)
@pytest.mark.django_db(transaction=True,reset_sequences=True)
def users_load():
    from apps.users.models import User

    def create_users():
        user_data = [
            {
                "id": "8aa34b1b-1499-41c6-a34b-1b1499b1c6d8",
                "email": "test@example.com",
                "password": "SomeSecurePassword12345!",
                "username": "anonymous",
            },
            {
                "id": "ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c",
                "email": "test_user@example.com",
                "password": "RandomPassword12345!",
                "username": "test_user",
            },
            {
                "id": "6bc9da01-9f4c-4338-89da-019f4ca33858",
                "email": "admin@example.com",
                "password": "AdminPassword12345!",
                "username": "admin",
            },
        ]

        for data in user_data:
            user = User.objects.create(
                **data,
            )
            user.set_password(data["password"])
            user.is_active = True
            user.save()

    create_users()


@pytest.fixture
@pytest.mark.django_db(transaction=True,reset_sequences=True)
def profiles_load(users_load):
    from apps.users.models import Profile, User

    def create_profiles():
        profiles_data = [
            {
                "id": 1,
                "first_name": "John",
                "last_name": "Doe",
                "user": User.objects.get(id="8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"),
            },
            {
                "id": 2,
                "first_name": "Jane",
                "last_name": "Doe",
                "user": User.objects.get(id="ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"),
            },
        ]

        for profile_data in profiles_data:
            user = profile_data.pop("user", None)
            profile = Profile.objects.create(
                user=user,
                **profile_data,
            )
            profile.save()

    create_profiles()


@pytest.fixture
@pytest.mark.django_db(transaction=True,reset_sequences=True)
def categories_load():
    from apps.attractions.models import Category

    def create_categories():
        categories_data = [
            {
                "name": "Museum",
                "description": "A place where historical, artistic, or scientific artifacts are exhibited."
            },
            {
                "name": "Library",
                "description": "A collection of books, documents, and other \
                informational resources available for public or private use."
            },
            {
                "name": "Park",
                "description": "An open green space with recreational areas, walking paths, and nature."
            },
            {
                "name": "Gallery",
                "description": "An exhibition space for displaying artworks, photography, and sculptures."
            },
            {
                "name": "Restaurant",
                "description": "A place where people can order and eat meals, \
                offering various cuisines and dining experiences."
            }
        ]
        for category_data in categories_data:
            category = Category.objects.create(
                **category_data,
            )
            category.save()

    create_categories()


@pytest.fixture
@pytest.mark.django_db(transaction=True,reset_sequences=True)
def attractions_load(users_load, categories_load):
    from apps.attractions.models import Attraction, Category
    from apps.users.models import User

    def create_attraction():
        attractions_data = [
            {
                "id": 1,
                "name": "Chick-fil-A",
                "description": "Some text",
                "longitude": -79.4132781,
                "latitude": 43.6428802,
                "open_hours": {
                    "monday": [
                        "08:00",
                        "17:00"
                    ],
                    "tuesday": [
                        "08:00",
                        "17:00"
                    ],
                    "wednesday": [
                        "08:00",
                        "17:00"
                    ],
                    "thursday": [
                        "08:00",
                        "17:00"
                    ],
                    "friday": [
                        "08:00",
                        "17:00"
                    ],
                    "saturday": [
                        "08:00",
                        "17:00"
                    ],
                    "sunday": [
                        "08:00",
                        "17:00"
                    ]
                },
                "address": "709 Yonge St, Toronto",
                "city": "New York",
                "country": "USA",
                "user": User.objects.get(id="8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"),
                "categories": [
                    Category.objects.get(name="Museum"), Category.objects.get(name="Library"),
                ]
            },
            {
                "id": 2,
                "name": "La Vecchia Restaurant",
                "description": "Some text",
                "longitude": -79.6101167,
                "latitude": 43.6548902,
                "open_hours": {},
                "address": "90 Marine Parade Dr, Etobicoke",
                "city": "New York",
                "country": "USA",
                "user": User.objects.get(id="ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"),
                "categories": [
                    Category.objects.get(name="Park"), Category.objects.get(name="Gallery"),
                ]
            },
            {
                "id": 3,
                "name": "Italian Kitchen",
                "description": "Some text",
                "longitude": -79.4080964,
                "latitude": 43.6448333,
                "open_hours": {},
                "address": "200 Front St W Unit #G001, Toronto",
                "city": "New York",
                "country": "USA",
                "user": User.objects.get(id="6bc9da01-9f4c-4338-89da-019f4ca33858"),
                "categories": [
                    Category.objects.get(name="Gallery"), Category.objects.get(name="Restaurant"),
                ]
            },
            {
                "id": 4,
                "name": "Windfield’s Restaurant",
                "description": "Some text",
                "longitude": -79.3873467,
                "latitude": 43.7266729,
                "open_hours": {},
                "address": "4261 Hwy 7, Unionville",
                "city": "New York",
                "country": "USA",
                "user": User.objects.get(id="ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"),
                "categories": []
            }
        ]
        for attraction_data in attractions_data:
            user = attraction_data.pop("user", None)
            categories_list = attraction_data.pop("categories", [])
            categories = []
            if categories_list:
                for category in categories_list:
                    categories.append(category)

            attraction = Attraction.objects.create(
                user=user,
                **attraction_data,
            )
            attraction.categories.set(categories) # noqa
            attraction.save()

    create_attraction()


@pytest.fixture
@pytest.mark.django_db(transaction=True,reset_sequences=True)
def reviews_load():
    from apps.threads.models import Review
    from apps.attractions.models import Attraction
    from apps.users.models import User

    def create_review():
        review_data = [
            {
                "id": "eed922f1-ed5d-4494-9922-f1ed5d44949c",
                "rating": 5,
                "price": 23.99,
                "time_spent": "01:00:00",
                "title": "Great Experience",
                "description": "It was a great experience. I highly recommend it.",
                "attraction": Attraction.objects.get(id=1),
                "user": User.objects.get(id="ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"),
            },
            {
                "id": "6753bd1d-9fb9-498a-93bd-1d9fb9498aff",
                "rating": 3,
                "price": 26.99,
                "time_spent": "02:00:00",
                "title": "Wonderful Experience",
                "description": "Wow, it was so amazing. I loved it.",
                "attraction": Attraction.objects.get(id=1),
                "user": User.objects.get(id="8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"),
            },
        ]
        for review_data in review_data:
            review = Review.objects.create(
                **review_data,
            )
            review.save()

    create_review()


@pytest.fixture
@pytest.mark.django_db(transaction=True,reset_sequences=True)
def comments_load():
    from apps.threads.models import Comment, Review
    from apps.users.models import User

    def create_comment():
        comment_data = [
            {
                "id": "b1135911-4fcc-4a08-9359-114fcc0a0893",
                "review": Review.objects.get(id="eed922f1-ed5d-4494-9922-f1ed5d44949c"),
                "user": User.objects.get(id="ad6b113f-1bcb-4f81-ab11-3f1bcbaf813c"),
                "content": "I really enjoyed my visit here. It was a great experience.",
            },
            {
                "id": "1520fda8-f043-4163-a0fd-a8f043c16359",
                "review": Review.objects.get(id="6753bd1d-9fb9-498a-93bd-1d9fb9498aff"),
                "user": User.objects.get(id="8aa34b1b-1499-41c6-a34b-1b1499b1c6d8"),
                "content": "Perfect place to visit. Highly recommended.",
            },
        ]
        for comment_data in comment_data:
            comment = Comment.objects.create(
                **comment_data,
            )
            comment.save()

    create_comment()


@pytest.fixture
@pytest.mark.django_db(transaction=True,reset_sequences=True)
def media_load():
    from apps.media.models import Media
    from apps.attractions.models import Attraction
    from apps.threads.models import Review, Comment

    def create_media():
        media_data = [
            {
                "id": "ad1329d9-e1a9-429e-9329-d9e1a9129ede",
                "file_url": "https://some_image/some_image.jpg",
                "bucket_name": "some_bucket",
                "file_name": "some_image.jpg",
                "file_type": "image/jpeg",
                "attraction": Attraction.objects.get(id=1),
                "review": None,
                "comment": None
            },
            {
                "id": "adaea95e-4793-4ed0-aea9-5e4793ced0da",
                "file_url": "https://rar_image/rar_image.jpg",
                "bucket_name": "rar_bucket",
                "file_name": "rar_image.jpg",
                "file_type": "image/jpeg",
                "attraction": Attraction.objects.get(id=1),
                "review": None,
                "comment": None
            },
            {
                "id": "77b2c935-a527-48f1-b2c9-35a52768f1db",
                "file_url": "https://dat_image/dat_image.jpg",
                "bucket_name": "dat_bucket",
                "file_name": "dat_image.jpg",
                "file_type": "image/jpeg",
                "attraction": Attraction.objects.get(id=2),
                "review": None,
                "comment": None
            },
            {
                "id": "7afafbb4-09f1-437b-bafb-b409f1937b48",
                "file_url": "https://wow_image/wow_image.webp",
                "bucket_name": "wow_bucket",
                "file_name": "wow_image.webp",
                "file_type": "image/webp",
                "attraction": None,
                "review": Review.objects.get(id="eed922f1-ed5d-4494-9922-f1ed5d44949c"),
                "comment": None
            },
            {
                "id": "409ad265-37a5-454f-9ad2-6537a5854f82",
                "file_url": "https://lol_image/lol_image.webp",
                "bucket_name": "lol_bucket",
                "file_name": "lol_image.webp",
                "file_type": "image/webp",
                "attraction": None,
                "review": None,
                "comment": Comment.objects.get(id="b1135911-4fcc-4a08-9359-114fcc0a0893")
            }
        ]
        for media_data in media_data:
            media = Media.objects.create(
                **media_data,
            )
            media.save()

    create_media()


@pytest.fixture
def user_db(request):
    from apps.users.models import User

    user_id = request.param
    return User.objects.get(id=user_id)


@pytest.fixture
def profile_db(request):
    from apps.users.models import Profile

    profile_id = request.param
    return Profile.objects.get(id=profile_id)


@pytest.fixture
def category_db(request):
    from apps.attractions.models import Category

    category_id = request.param

    return Category.objects.get(id=category_id)


@pytest.fixture
def attraction_db(request):
    from apps.attractions.models import Attraction

    attraction_id = request.param

    return Attraction.objects.get(id=attraction_id)


@pytest.fixture
def media_db(request):
    from apps.media.models import Media

    media_id = request.param

    return Media.objects.get(id=media_id)


@pytest.fixture
def review_db(request):
    from apps.threads.models import Review

    review_id = request.param

    return Review.objects.get(id=review_id)


@pytest.fixture
def comment_db(request):
    from apps.threads.models import Comment

    comment_id = request.param

    return Comment.objects.get(id=comment_id)
