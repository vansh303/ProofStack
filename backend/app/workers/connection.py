import os

from redis import Redis


def get_redis_connection() -> Redis:
    redis_url = os.getenv("REDIS_URL")

    if not redis_url:
        raise RuntimeError("REDIS_URL is not configured.")

    return Redis.from_url(redis_url)
