from fastapi import APIRouter, Depends, HTTPException, status
from .dependencies import get_redis
from redis import Redis
from fastapi import Request
from datetime import datetime
from config import settings

router: APIRouter = APIRouter()


@router.get("/")
def main(request: Request, redis: Redis = Depends(get_redis)):
    ip = request.client.host
    now = datetime.utcnow()
    if redis.exists(ip):
        prev = redis.get(ip)
        prev = datetime.fromisoformat(prev.decode("utf-8"))
        seconds = (now - prev).total_seconds()
        if seconds < settings.time_delay:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Слишком частое обращение"
            )
        else:
            redis.set(ip, now.isoformat())
    else:
        redis.set(ip, now.isoformat())

    return {"message": "ok"}
