from llm import get_llm
from prompts import FINAL_ANSWER_PROMPT
from tools.calculator import calculator_tool
from tools.search import research_search_tool
from tools.summarizer import summarizer_tool
from tools.code_helper import code_helper_tool
from agents.router_agent import RouterAgent
from schemas import AgentResponse
from logger import log_event


class ResearchAgent:
    def __init__(self):
        self.router = RouterAgent()
        self.llm = get_llm(temperature=0.2)

    def execute_tool(self, route: str, tool_input: str) -> str:
        if route == "math":
            return calculator_tool(tool_input)

        if route == "research":
            return research_search_tool(tool_input)

        if route == "coding":
            return code_helper_tool(tool_input)

        if route == "summary":
            return summarizer_tool(tool_input)

        return "No external tool required."

    def generate_final_answer(
        self,
        query: str,
        route: str,
        tool_output: str
    ) -> str:
        prompt = FINAL_ANSWER_PROMPT.format(
            query=query,
            route=route,
            tool_output=tool_output
        )

        response = self.llm.invoke(prompt)
        return response.content

    def run(self, query: str) -> AgentResponse:
        decision = self.router.route(query)

        tool_output = self.execute_tool(
            route=decision.route,
            tool_input=decision.tool_input
        )

        final_answer = self.generate_final_answer(
            query=query,
            route=decision.route,
            tool_output=tool_output
        )

        response = AgentResponse(
            query=query,
            route=decision.route,
            tool_input=decision.tool_input,
            tool_output=tool_output,
            final_answer=final_answer,
            confidence=decision.confidence,
            reason=decision.reason
        )

        log_event("QUERY", query)
        log_event("ROUTE_DECISION", decision.model_dump_json(indent=2))
        log_event("TOOL_OUTPUT", tool_output)
        log_event("FINAL_ANSWER", final_answer)

        return response