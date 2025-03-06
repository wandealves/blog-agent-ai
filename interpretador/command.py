from crewai import Agent, Task, Crew, Process, LLM
from cli_tool import CLITool

class Command:

    def __init__(self):
        self.llm = LLM(model="openai/gpt-4o-mini", )
        self.cli = CLITool()
        self.create_crew()

    def create_crew(self):
        """Agent Software Engineer."""
        self.software_engineer = Agent(
          role="Software Engineer",
          goal="Always use Executor Tool. Ability to perform CLI operations, write programs and execute using Exector Tool",
          backstory='Expert in command line operations, creating and executing code.',
          tools=[self.cli.execute_cli_command],
          llm=self.llm,
          verbose=True
        )
        self.software_engineer_task = Task(
          description="Execute the command {command} using the Executor Tool.",
          expected_output="The expected output of the executed CLI command.",
          agent=self.software_engineer,
          tools=[self.cli.execute_cli_command],
          verbose=True
        )
        self.crew = Crew(
          agents=[self.software_engineer],
          tasks=[ self.software_engineer_task],
          process=Process.sequential,
          manager_llm=self.llm,
          verbose=True
        )

    def kickoff(self, inputs):
        result = self.crew.kickoff(inputs=inputs)
        return result