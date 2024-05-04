# python
import asyncio
import datetime
import json

# Django
from channels.consumer import AsyncConsumer, SyncConsumer
from channels.generic.http import AsyncHttpConsumer

# Local
from projectapp.models import LearningPath


class SimpleLearningPathConsumer(AsyncConsumer):
    async def print_learningpath(self, message):
        print(f"WORKER: LearningPath: {message['data']}")


class LearningPathConsumer(AsyncHttpConsumer):
    async def handle(self, body):
        # Get all learning paths
        learningpaths = LearningPath.objects.all()
        # Serialize the learning paths
        data = json.dumps(
            [{"title": LearningPath.title, "url": LearningPath.url} for LearningPath in learningpaths]
        )
        # Send the serialized data as a JSON response
        await self.send_response(
            200, data, headers=[(b"Content-Type", b"application/json")]
        )

    # Server-send event https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events
    async def handle(self, body):
        await self.send_headers(
            headers=[
                (b"Cache-Control", b"no-cache"),
                (b"Content-Type", b"text/event-stream"),
                (b"Transfer-Encoding", b"chunked"),
            ]
        )
        while True:
            payload = "data: %s\n\n" % datetime.now().isoformat()
            await self.send_body(payload.encode("utf-8"), more_body=True)
            await asyncio.sleep(1)

    async def send_learning_path(self, bookmark):
        # Serialize the bookmark
        data = json.dumps({"title": LearningPath.title})
        # Send the serialized data as a JSON response
        await self.channel_layer.send(
            "learningpath-add", {"type": "send.learningpath", "data": data}
        )
        # await self.send_response(
        #     200, data, headers=[(b"Content-Type", b"application/json")]
        # )
