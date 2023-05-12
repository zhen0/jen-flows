from prefect import flow
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class Param(BaseModel):
    some_complex_object: Optional[List[Dict[str, Any]]] = Field(
                title="some_complex_object",
                default=None,
            )

@flow(
    name="CopyPydanticModelUITest",
    log_prints=True
)
def main(
    config: Param = Param(
        some_complex_object=[
            {
                "foo": "foo1",
                "bar": "bar1",
                "foo_bar": "foo_bar1"
            },
            {
                "foo": "foo2",
                "bar": "bar2",
                "foo_bar": "foo_bar2"
            }
        ]
    )
) -> None:
    print(config)


if __name__ == "__main__":
    main()