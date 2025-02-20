from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import RegisterView as BaseRegisterView
from dj_rest_auth.registration.views import SocialConnectView
from dj_rest_auth.views import LoginView as BaseLoginView
from drf_spectacular.utils import OpenApiExample, extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.auth.serializers import MFASetupSerializer, MFAVerifySerializer, MFAStatusSerializer
from allauth.mfa.adapter import get_adapter

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


class MFASetupView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MFASetupSerializer


class MFAVerifyView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MFAVerifySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'status': 'verified'})


class MFAStatusView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MFAStatusSerializer

    def get_object(self):
        adapter = get_adapter()
        return {
            'mfa_enabled': adapter.is_mfa_enabled(self.request.user),
            'type': 'totp'
        }