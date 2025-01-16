from dataclasses import dataclass
from typing import List, Optional
from rich.console import Console
from rich.panel import Panel


@dataclass
class Interaction:
    question: str
    response: str


_INTERACTION_TEMPLATE = """
Question: {}
Response: {}
"""


class Session:
    def __init__(self, session_id: str, console: Console = Console(color_system="truecolor")) -> None:
        self.interactions: List[Interaction] = []
        self.session_id = session_id
        self.console = console

    def add_interaction(self, question: str, response: str) -> None:
        self.interactions.append(Interaction(question, response))

    def print_interactions(self) -> None:
        formated_interactions = [
            _INTERACTION_TEMPLATE.format(interaction.question, interaction.response)
            for interaction in self.interactions
        ]
        panel = Panel("\n".join(formated_interactions), title=f"Session {self.session_id}")
        self.console.print(panel)
