from prefect import flow

@flow(log_prints=True, name="hi_flow")
def hi_flow():
    '''Very basic flow created using prefect projects. Should print "Hi from Prefect! 🤗" 
    ```python
    from prefect import flow

    @flow(log_prints=True, name="hi_flow")
    def hi_flow():
        print("Hi from Prefect! 🤗")
        ```
    Code is in hello.py in jen_flows

    To create a deployment run:
    ```bash
    prefect create project "jen_flows"
    prefect deploy ./hello.py:hi_flow \
    -n hi-flow-deployment \
    -p process
    '''
    print("Hi from Prefect! 🤗")

