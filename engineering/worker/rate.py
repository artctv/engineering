
from fastapi import FastAPI, Request, HTTPException, status, Depends
from datetime import datetime, timedelta
import time
from redis import Redis
from rq import Queue

# app: FastAPI = FastAPI()

time = {}


def timeout():
    queue = Queue(connection=Redis())
    if queue in time:
        prev = time[queue]
        now = datetime.utcnow()
        to_redis = now.isoformat()
        seconds = (now - prev).total_seconds()
        x = datetime.fromisoformat(to_redis)
        v = now - x
        v.total_seconds()
        if seconds < 5:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Слишком частое обращение"
            )
        else:
            time[queue] = datetime.now()
    else:
        time[queue] = datetime.now()

