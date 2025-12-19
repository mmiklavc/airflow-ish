from datetime import timedelta
from airflow import DAG
from cloudera.airflow.providers.operators.cde import CdeRunJobOperator
import pendulum

default_args = {
    'retry_delay': timedelta(seconds=5),
    'depends_on_past': False,
    'start_date': pendulum.datetime(2021, 1, 1, tz="UTC")
}

example_dag = DAG(
    'example-cdeoperator',
    default_args=default_args,
    schedule='@once',
    catchup=False,
    is_paused_upon_creation=False
)

step1 = CdeRunJobOperator(
    connection_id='kesha-blah-blah-blah',
    task_id='ingest',
    retries=3,
    dag=example_dag,
    job_name='pi-calculator',
    queue='kubernetes',
    pool='default_pool'
)

step1
