from time import sleep
from typing import List

from prefect import flow, get_run_logger, task
from prefect.deployments import run_deployment

@flow(name="childFlow")
def basic():
    logthis("I'm a child")

@flow(name="depFlow")
def example1():
    response = run_deployment(name="aa5426d9-7b1b-4cf2-a721-a83aab7073cc")
    print(response)

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
    example1()

if __name__ == "main":
    basic_flow(28)
