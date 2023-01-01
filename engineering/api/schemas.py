from pydantic import BaseModel, UUID4
from rq.job import JobStatus


class ResponsePredict(BaseModel):
    id: UUID4
    status: JobStatus
