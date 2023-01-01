from typing import Optional
from pydantic import BaseModel
from rq.job import JobStatus


class ResponseRetrieve(BaseModel):
    status: JobStatus
    result: Optional[str]
