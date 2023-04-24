from prefect import flow
from pydantic import Json


@flow
def param_example(
    param: Json = '[{"a": 1}]'
) -> None:
    pass

# if __name__ == "__main__":
#     param_example()