from rq import Queue
from app.workers.connection import get_redis_connection

def get_default_queue() -> Queue:
    return Queue(
        name="default",
        connection=get_redis_connection(),
    )