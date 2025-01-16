from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import NL2SQLTool
from crewai_tools import MySQLSearchTool
from crewai_tools import PGSearchTool

@CrewBase
class SqlQueryCrewFormationAndTaskCoordinationCrew():
    """SqlQueryCrewFormationAndTaskCoordination crew"""

    @agent
    def query_builder(self) -> Agent:
        return Agent(
            config=self.agents_config['query_builder'],
            tools=[PGSearchTool(db_uri="postgresql://postgres:postgres@localhost:5432/crewai", table_name="sales"),],
        )

    @agent
    def query_executor(self) -> Agent:
        return Agent(
            config=self.agents_config['query_executor'],
            tools=[NL2SQLTool(db_uri="postgresql://postgres:postgres@localhost:5432/crewai")],
        )

    @agent
    def output_formatter(self) -> Agent:
        return Agent(
            config=self.agents_config['output_formatter'],
            
        )


    @task
    def create_sql_query_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_sql_query_task'],
            tools=[PGSearchTool(
                table_name="sales",
                db_uri="postgresql://postgres:postgres@localhost:5432/crewai",
            )],
        )

    @task
    def execute_sql_query_task(self) -> Task:
        return Task(
            config=self.tasks_config['execute_sql_query_task'],
            tools=[NL2SQLTool(db_uri="postgresql://postgres:postgres@localhost:5432/crewai")],
        )

    @task
    def format_query_output_task(self) -> Task:
        return Task(
            config=self.tasks_config['format_query_output_task'],
            
        )


    @crew
    def crew(self) -> Crew:
        """Creates the SqlQueryCrewFormationAndTaskCoordination crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            planning=True,
        )
