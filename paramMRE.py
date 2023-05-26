from prefect import flow
from pydantic import BaseModel, Json, HttpUrl


class Param(BaseModel):
    foo: list
    bar: dict
    car: HttpUrl
    foo_bar: Json

@flow(
    name="PydanticModelUITest",
)
def paramMRE(
    param: Param,
    URL: HttpUrl = "http://www.example.com",
    param_with_runtime_defaults: Param = Param(foo=[1], bar={"foo": 1}, car="http://www.example.com", foo_bar="[1]")
) -> None:
    pass


if __name__ == "__main__":
    paramMRE(Param(foo=[1], bar={"foo": 1}, car="http://www.example.com", foo_bar="[1]"))