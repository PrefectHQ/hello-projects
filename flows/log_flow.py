import sys
from utilities import AN_IMPORTED_MESSAGE

import prefect
from prefect import flow, task, get_run_logger


@task
def log_task(name):
    logger = get_run_logger()
    logger.info("Hello %s!", name)
    logger.info("Prefect Version = %s 🚀", prefect.__version__)
    logger.debug(AN_IMPORTED_MESSAGE)


@flow
def log_flow(name: str = "Marvin"):
    log_task(name)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        log_flow(name)
    else:
        log_flow()
