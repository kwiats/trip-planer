from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import RegisterView as BaseRegisterView
from dj_rest_auth.registration.views import SocialConnectView
from dj_rest_auth.views import LoginView as BaseLoginView
from drf_spectacular.utils import OpenApiExample, extend_schema


@extend_schema(
    tags=["auth"],
    examples=[
        OpenApiExample(
            "Register",
            value={
                "username": "some_username",
                "email": "email@email.com",
                "password": "password12345!",
                "rewrite_password": "password12345!",
            },
        ),
    ],
)
class RegisterView(BaseRegisterView):
    pass


@extend_schema(
    tags=["auth"],
    examples=[
        OpenApiExample(
            "Login",
            value={
                "email": "email@email.com",
                "password": "password12345!",
            },
        ),
    ],
)
class LoginView(BaseLoginView):
    pass


@extend_schema(
    tags=["auth"],
    examples=[
        OpenApiExample(
            "Connect",
            value={
                "provider": "github",
            },
        ),
    ],
)
class GitHubConnectView(SocialConnectView):
    adapter_class = GitHubOAuth2Adapter
    client_class = OAuth2Client
    # callback_url = os.environ("GITHUB_CALLBACK_URL")


@extend_schema(
    tags=["auth"],
    examples=[
        OpenApiExample(
            "Connect",
            value={
                "provider": "facebook",
            },
        ),
    ],
)
class FacebookConnectView(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter
