from prefect import flow

@flow(log_prints=True, name="hi_flow")
def hi_flow():
    print("Hi from Prefect! 🤗")

