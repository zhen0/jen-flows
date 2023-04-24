from prefect import flow, task, get_run_logger
import time
@task
def append_1(num: str):
    time.sleep(6)
    return num + "1"

@task
def append_2(num: str):
    time.sleep(6)
    return num + "2"

@task
def append_num(num: str, append_with: str):
    time.sleep(6)
    return num + append_with

@task
def convert_str_to_int(num: str):
    time.sleep(6)
    return int(num)

from prefect.engine import pause_flow_run
@flow()
def pause_example(num: str):
    x = append_1.submit(num)
    y = append_2.submit(x.result())
    z = append_num.submit(y.result(), "12")
    logger = get_run_logger()
    logger.info(f"First result: {convert_str_to_int(x.result())}")
    # pause_flow_run(timeout=30)
    logger.info(f"Second result: {convert_str_to_int(y.result())}")
    logger.info(f"Third result: {convert_str_to_int(z.result())}")

# minimal_reproducible_pause_example(30)
# The line pause_flow_run(timeout=30) is commented out, but we'll come back to this later. This is a minimal flow that, when run perfectly, will generate the DAG attached in the bug summary section.