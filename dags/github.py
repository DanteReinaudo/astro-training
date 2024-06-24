from airflow.decorators import dag, task
from datetime import datetime


@dag(schedule=None, catchup=False, default_args={"retries": 2}, tags=["example"])
def github():

    @task
    def my_task():
        print("Hello World!")

    my_task()


github()
