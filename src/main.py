import json
from datetime import date

from rich.console import Console

from sql_query_crew_formation_and_task_coordination.crew import SqlQueryCrewFormationAndTaskCoordinationCrew
from sql_query_crew_formation_and_task_coordination.main import run
from support.sales_db import init_db_with_fake_data, Sales


DB_FILE_NAME = "postgres:postgres@localhost:5432/crewai"

def main():
    console = Console(color_system="truecolor")

    console.rule("Initializing the database")
    init_db_with_fake_data(
        db_file_name=DB_FILE_NAME,
        db_data=[
            Sales(id="1", customer_name="John", date=date(2024, 1, 1), price=20),
            Sales(id="2", customer_name="Alice", date=date(2024, 1, 2), price=30),
            Sales(id="3", customer_name="Bob", date=date(2024, 7, 1), price=35),
        ]
    )
    print(f"DB initialized with fake data in {DB_FILE_NAME}")

    crew = SqlQueryCrewFormationAndTaskCoordinationCrew().crew()

    question = "which customer made the biggest sale?"

    inputs = {
        'user_request': question,
        'database_schema': '',
        'sql_query': '',
        'query_output': ''
    }
    crew.kickoff(inputs=inputs)


if __name__ == '__main__':
    main()