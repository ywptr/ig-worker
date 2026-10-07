import asyncio
import logging
import os

from vercel.queue import (
    ALL_DEPLOYMENTS,
    QueueClient,
)

from app.core.logging import configure_logging
from worker import process_job


configure_logging()

logger = logging.getLogger(__name__)


def get_queue_client() -> QueueClient:
    kwargs = {
        "deployment": ALL_DEPLOYMENTS,
    }

    if region := os.getenv("VERCEL_REGION"):
        kwargs["region"] = region

    if token := os.getenv("VERCEL_OIDC_TOKEN"):
        kwargs["token"] = token

    if base_url := os.getenv("IG_QUEUE_BASE_URL"):
        kwargs["base_url"] = base_url

    return QueueClient(**kwargs)


async def main() -> None:
    logger.info("queue.poller.start topic=ig-jobs")

    client = get_queue_client()

    await client.poll_and_handle(
        process_job,
        topics=["ig-jobs"],
        interval=1.0,
    )


if __name__ == "__main__":
    asyncio.run(main())
