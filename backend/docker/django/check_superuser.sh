#!/bin/bash
# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# fail exit if one of your pipe command fails
set -o pipefail
# exits if any of your variables is not set
set -o nounset

# function checks if admin user exists
admin_exists() {
    python <<END
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()
if User.objects.filter(is_superuser=True).exists():
    print("True")
else:
    print("False")
END
}

# function creates superuser
install_superuser() {
    python <<END
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()
try:
    user = User.objects.create_superuser(
        username=os.environ["DJANGO_SUPERUSER_USERNAME"],
        email=os.environ["DJANGO_SUPERUSER_EMAIL"],
        password=os.environ["DJANGO_SUPERUSER_PASSWORD"],
    )
    print(f"Superuser {user.username} created successfully.")
except Exception as e:
    print(f"Error creating superuser: {e}")
    raise
END
}


if [[ $(admin_exists) == "False" ]]; then
    echo "Admin user does not exist. Creating..."
    install_superuser
else
    echo "Admin user already exists. No action required."
fi