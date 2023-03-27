from prefect import flow, task
from prefect.filesystems import GitHub, S3

gh_block = GitHub.load("jen-gh")
s3_block = S3.load("jen-s3")


@task
def hello_dict():
    print('hello from dict task')
    return {'description': "hello"}

@task
def hello_string():
    print('hello from string task')
    return 'hello'

@task
def hello_int(persist_result=True):
    print('hello from int task')
    return 8

@task
def hello_bool(persist_result=True):
    print('hello from bool task')
    return False

@flow(log_prints=True, persist_result=True, result_storage=s3_block, result_serializer='json', name="hi_results")
def hi_results():
    hello_dict()
    hello_string()
    hello_int()
    hello_bool()
    print("Hi from flow")
    return 'hi flow string'

