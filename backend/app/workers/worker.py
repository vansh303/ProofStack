from redis import Redis
from rq import Worker
from app.workers.connection import get_redis_connection

def create_worker() -> Worker:
    redis_connection: Redis = get_redis_connection()
    return Worker(
        queues=["default"],
        connection=redis_connection,
    )

if __name__=="__main__":
    worker = create_worker()
    worker.work()