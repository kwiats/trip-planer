from enum import Enum


class BucketNames(Enum):
    ATTRACTIONS = "attractions"
    COMMENTS = "comments"
    REVIEWS = "reviews"
    USERS = "users"


class BucketNamesID(Enum):
    ATTRACTIONS = "attraction_id"
    COMMENTS = "comment_id"
    REVIEWS = "review_id"
    USERS = "user_id"
