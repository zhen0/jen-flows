from prefect import flow, task, pause_flow_run
from prefect.filesystems import GitHub, S3

# gh_block = GitHub.load("jen-gh")
s3_block = S3.load("jen-s3")


@task(persist_result=False)
def hello_dict_no_persist():
    print('hello from dict task')
    return {'description': "hello"}

@task(persist_result=True)
def hello_dict():
    print('hello from dict task')
    return {'description': "hello"}

@task(persist_result=True, result_storage_key="default-storage.json")
def hello_string(word):
    print('hello from string task', word)
    return 'hello'

@task(persist_result=True, result_serializer='json', )
def hello_int():
    print('hello from int task')
    return 8

@task
def hello_bool(persist_result=True):
    print('hello from bool task')
    return False

@flow(log_prints=True, persist_result=True, result_serializer='json', name="hi_results")
# @flow(log_prints=True, persist_result=True, result_storage=s3_block, result_serializer='json', name="hi_results")
def hi_results(word:str='default'):
    hello_dict()
    hello_string(word)
    hello_int()
    hello_bool()
    pause_flow_run(timeout=300)
    print("Hi from paused flow")
    return 'hi flow string'

# hi_results()
