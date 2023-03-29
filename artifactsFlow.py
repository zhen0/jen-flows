from prefect.experimental.artifacts import create_table_artifact, create_link_artifact, create_markdown_artifact
from prefect import task, flow

@task(persist_result=True)
def my_fn():
    highest_churn_possibility = [
       {'customer_id':'12345', 'name': 'John Smith', 'churn_probability': 0.85 }, 
       {'customer_id':'56789', 'name': 'Jane Jones', 'churn_probability': 0.65 } 
    ]

    artId= create_table_artifact(
        key="personalized-reachout",
        table=highest_churn_possibility,
        description= "# Marvin, please reach out to these customers today!"
    )
    return artId


@task(persist_result=True)
def my_special_task(persist_result=True):
    artifact_id = create_link_artifact(
        key="my-important-link-2",
        link="s3://my-bucket/my-key",
        link_text="s3-bucket",
        description="This creates a link to my important bucket.",
    )
    return artifact_id

@flow(persist_result=True)
def my_flow(persist_result=True):
    my_special_task()
    my_fn()
    create_markdown_artifact(
        key="important-markdown-2",
        markdown="# List of important ducks: 1. Marvin",
        description="Everything you need to know",
    )


if __name__ == "__main__":
    my_flow()


