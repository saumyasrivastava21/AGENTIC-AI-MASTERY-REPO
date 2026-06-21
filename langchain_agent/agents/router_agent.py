from llm import get_llm
from schemas import RouteDecision
from prompts import ROUTER_SYSTEM_PROMPT


class RouterAgent:
    def __init__(self):
        llm = get_llm(temperature=0.0)
        self.structured_llm = llm.with_structured_output(RouteDecision)

    def route(self, query: str) -> RouteDecision:
        messages = [
            ("system", ROUTER_SYSTEM_PROMPT),
            ("human", query)
        ]

        return self.structured_llm.invoke(messages)