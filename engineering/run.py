import uvicorn
from rq import Connection, Worker
from typer import Typer, Argument
from typing import Optional, NoReturn
from config import settings
from worker.worker import run as run_worker


cli: Typer = Typer()


@cli.command()
def main(worker: Optional[str] = Argument(None)):
    if worker:
        run_worker()
    else:
        uvicorn.run(
            "api.app:app",
            host=settings.api.host,
            port=settings.api.port,
            reload=settings.api.reload
        )


if __name__ == "__main__":
    cli()
