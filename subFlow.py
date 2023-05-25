from time import sleep
from typing import List

from prefect import flow, get_run_logger, task

@flow(name="childFlow")
def basic():
    logthis("I'm a child")

@task
def logthis(x):
    logger = get_run_logger()
    logger.warning(x)

@task
def setup() -> None:
    logger = get_run_logger()
    logger.info("setup start")
    # sleep(1) won't hang
    sleep(8)
    logger.info("setup end")


@task
def fetch_batches(rangeInt:int) -> List[str]:
    # using range(30) here won't hang
    return [f"batch {i}" for i in range(rangeInt)]


@task
def count_rows(batch: str) -> int:
    logger = get_run_logger()
    logger.info(f"{batch}")
    return 1


@flow
def map_flow(rangeInt) -> None:
    batches = fetch_batches.submit(rangeInt)
    count_rows.map(batches, wait_for=[setup.submit()])  # type: ignore
    


@flow(name="test-sub")
def basic_flow(rangeInt:int=28):
    logthis('base')
    basic()
    map_flow(rangeInt)

if __name__ == "main":
    basic_flow(28)
