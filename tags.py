from datetime import datetime
from time import sleep

from prefect import flow
from prefect import task
from prefect.task_runners import SequentialTaskRunner


@task(tags=["test"])
def test_task(n):
    print(f"Starting {n} at {datetime.now()}")
    sleep(10)
    print(f"Ending {n} at {datetime.now()}")


@flow(task_runner=SequentialTaskRunner())
def test_flow():
    test_task.map([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# if __name__ == "__main__":
#     test_flow()