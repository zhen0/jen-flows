from prefect.artifacts import create_table_artifact, create_link_artifact, create_markdown_artifact
from prefect import task, flow
import markdown

@task()
def table_task():
    highest_churn_possibility = {
        'customer_id': ['123456789', '987654321', '246810121', '135791113', '864208046'],
        'name': ['John Smith', 'Jane Doe', 'Bob Johnson', 'Sarah Jones', 'Tom Wilson'],
        'churn_probability': [0.85, 0.79, 0.67, 0.61, 0.57]
    }
    create_table_artifact(
        key="personalized-reachout",
        table=highest_churn_possibility,
        description= "# Marvin, please reach out to these customers today!"
    )

@task()
def link_task():
    artifact_id = create_link_artifact(
        key="my-important-link-2",
        link="s3://my-bucket/my-key",
        link_text="s3-bucket",
        description="This creates a link to my important bucket.",
    )
    return artifact_id

@task
def my_task():
    na_revenue = 500000
    markdown_report = f"""
        # Sales Report

        ## Summary

        In the past quarter, our company saw a significant increase in sales, with a total revenue of $1,000,000. This represents a 20% increase over the same period last year.

        ## Sales by Region

        | Region        | Revenue |
        |:--------------|-------:|
        | North America | 5000 |
        | Europe        | $250,000 |
        | Asia          | $150,000 |
        | South America | $75,000 |
        | Africa        | $25,000 |

        ## Top Products

        1. Product A - $300,000 in revenue
        2. Product B - $200,000 in revenue
        3. Product C - $150,000 in revenue

        ## Conclusion

        Overall, these results are very encouraging and demonstrate the success of our sales team in increasing revenue across all regions. However, we still have room for improvement and should focus on further increasing sales in the coming quarter.
        """
    return markdown_report

@flow()
def my_flow():
    # table_task()
    # link_task()
    my_important_report = my_task()
    # report = markdown_task(),
    create_markdown_artifact(
        key="important-markdown-2",
        markdown=my_important_report,
        description="Everything you need to know",
    )


if __name__ == "__main__":
    my_flow()


