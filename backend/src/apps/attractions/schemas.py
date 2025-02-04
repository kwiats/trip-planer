from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiExample, OpenApiParameter

attraction_examples = {
    "attraction-create": [
OpenApiExample(
                "Chick-fil-A",
                value={
                    "name": "Chick-fil-A",
                    "description": "Some text",
                    "longitude": -79.4132781,
                    "latitude": 43.6428802,
                    "open_hours": {
                        "monday": ["08:00", "17:00"],
                        "tuesday": ["08:00", "17:00"],
                        "wednesday": ["08:00", "17:00"],
                        "thursday": ["08:00", "17:00"],
                        "friday": ["08:00", "17:00"],
                        "saturday": ["08:00", "17:00"],
                        "sunday": ["08:00", "17:00"],
                    },
                    "address": "709 Yonge St, Toronto",
                    "city": "New York",
                    "country": "USA",
                    "add_categories": ["Culture", "Landmark"],
                },
            ),
            OpenApiExample(
                "La Vecchia Restaurant",
                value={
                    "name": "La Vecchia Restaurant",
                    "description": "Some text",
                    "longitude": -79.6101167,
                    "latitude": 43.6548902,
                    "open_hours": {},
                    "address": "90 Marine Parade Dr, Etobicoke",
                    "city": "New York",
                    "country": "USA",
                    "add_categories": ["Restaurant"],
                },
            ),
            OpenApiExample(
                "Smash Kitchen",
                value={
                    "name": "Smash Kitchen",
                    "description": "Some text",
                    "longitude": -79.5045743,
                    "latitude": 43.7589809,
                    "open_hours": {},
                    "address": "90 Marine Parade Dr, Etobicoke",
                    "city": "New York",
                    "country": "USA",
                    "add_categories": ["Restaurant"],
                },
            ),
            OpenApiExample(
                "Windfield’s Restaurant",
                value={
                    "name": "Windfield’s Restaurant",
                    "description": "Some text",
                    "longitude": -79.3873467,
                    "latitude": 43.7266729,
                    "open_hours": {},
                    "address": "4261 Hwy 7, Unionville",
                    "city": "New York",
                    "country": "USA",
                    "add_categories": ["Restaurant"],
                },
            ),
            OpenApiExample(
                "Italian Kitchen",
                value={
                    "name": "Italian Kitchen",
                    "description": "Some text",
                    "longitude": -79.4080964,
                    "latitude": 43.6448333,
                    "open_hours": {},
                    "address": "200 Front St W Unit #G001, Toronto",
                    "city": "New York",
                    "country": "USA",
                    "add_categories": ["Restaurant"],
                },
            ),
    ]
}

attraction_parameters = {
    "attraction-retrieve": [
OpenApiParameter(
                name="country",
                description="Filter attractions by country name.",
                required=False,
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="city",
                description="Filter attractions by city name.",
                required=False,
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="latitude",
                description="Latitude for filtering attractions by location.",
                required=False,
                type=OpenApiTypes.NUMBER,
                examples=[OpenApiExample("Example Latitude", value=43.65)],
            ),
            OpenApiParameter(
                name="longitude",
                description="Longitude for filtering attractions by location.",
                required=False,
                type=OpenApiTypes.NUMBER,
                examples=[OpenApiExample("Example Longitude", value=-79.42)],
            ),
            OpenApiParameter(
                name="radius",
                description="Radius (in kilometers) around the specified latitude and longitude. Default is 10 km.",
                required=False,
                type=OpenApiTypes.NUMBER,
                default=10000,
            ),
            OpenApiParameter(
                name="category",
                description="Filter attractions by category name (e.g., 'Park', 'Museum').",
                required=False,
                type=OpenApiTypes.STR,
            ),
            OpenApiParameter(
                name="sort_by",
                description="Sort results by criteria: 'topRated' or 'mostRated'. Default is 'topRated'.",
                required=False,
                type=OpenApiTypes.STR,
                enum=["topRated", "mostRated"],
                default="topRated",
            ),
            OpenApiParameter(
                name="sort_direction",
                description="Sort direction: 'asc' (ascending) or 'desc' (descending). Default is 'desc'.",
                required=False,
                type=OpenApiTypes.STR,
                enum=["asc", "desc"],
                default="desc",
            ),
    ]
}