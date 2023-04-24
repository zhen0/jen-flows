from prefect import flow, task, get_run_logger
import time
@task
def append_1(num: str, num2: int):
    time.sleep(num2)
    return num + "1"

@task
def append_2(num: str, num2: int):
    time.sleep(num2)
    return num + "2"

@task
def append_num(num: str, append_with: str, num2: int):
    time.sleep(num2)
    return num + append_with

@task
def convert_str_to_int(num: str):
    time.sleep(6)
    return int(num)

from prefect.engine import pause_flow_run
@flow(persist_result=True)
def pause_example(num: str, num2: int = 30):
    x = append_1.submit(num, num2)
    y = append_2.submit(x.result(), num2)
    z = append_num.submit(y.result(), "12", num2)
    logger = get_run_logger()
    logger.info(f"First result: {convert_str_to_int(x.result())}")
    # pause_flow_run(timeout=300)
    logger.info(f"Second result: {convert_str_to_int(y.result())}")
    logger.info(f"Third result: {convert_str_to_int(z.result())}")

# pause_example(30)
# The line pause_flow_run(timeout=30) is commented out, but we'll come back to this later. This is a minimal flow that, when run perfectly, will generate the DAG attached in the bug summary section.