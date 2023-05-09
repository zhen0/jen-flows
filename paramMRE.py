from prefect import flow
from pydantic import BaseModel, Json


class Param(BaseModel):
    foo: list
    bar: dict
    foo_bar: Json

@flow(
    name="PydanticModelUITest",
)
def paramMRE(
    param: Param,
    param_with_runtime_defaults: Param = Param(foo=[1], bar={"foo": 1}, foo_bar="[1]")
) -> None:
    pass


# if __name__ == "__main__":
#     main()