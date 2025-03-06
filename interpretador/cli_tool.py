from crewai.tools import tool
from interpreter import interpreter

class CLITool:

    interpreter.auto_run = True
    interpreter.llm.model = "openai/gpt-4o-mini"

    @tool("executor")
    def execute_cli_command(command:str):
        """Create an Execute code using Open Interpreter."""
        result = interpreter.chat(command)
        return result