"""
ASGI config for finalproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ChannelNameRouter, ProtocolTypeRouter

from projectapp import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finalproject.settings')

project_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": project_asgi_app,
        "channel": ChannelNameRouter(
            {
                "learningpath-add": consumers.SimpleLearningPathConsumer.as_asgi(),
            }
        ),
    }
)
