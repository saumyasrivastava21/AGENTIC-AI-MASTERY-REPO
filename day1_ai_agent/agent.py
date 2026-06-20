import json
from llm import get_llm
from prompts import ROUTER_PROMPT, FINAL_PROMPT
from tools import calculator, mock_search, get_current_time, summarize_text


class SimpleAIAgent:
    def __init__(self):
        self.llm = get_llm(temperature=0.2)

    def parse_json(self, text: str) -> dict:
        try:
            start = text.find("{")
            end = text.rfind("}") + 1

            if start == -1 or end == -1:
                raise ValueError("No JSON found")

            json_text = text[start:end]
            return json.loads(json_text)

        except Exception:
            return {
                "tool": "none",
                "tool_input": "",
                "reason": "Failed to parse JSON, answering directly."
            }

    def choose_tool(self, query: str) -> dict:
        prompt = ROUTER_PROMPT.format(query=query)
        response = self.llm.invoke(prompt)
        return self.parse_json(response.content)

    def run_tool(self, tool_name: str, tool_input: str) -> str:
        if tool_name == "calculator":
            return calculator(tool_input)

        if tool_name == "search":
            return mock_search(tool_input)

        if tool_name == "time":
            return get_current_time(tool_input)

        return "No tool used."

    def final_answer(
        self,
        query: str,
        tool: str,
        tool_result: str
    ) -> str:
        prompt = FINAL_PROMPT.format(
            query=query,
            tool=tool,
            tool_result=tool_result
        )

        response = self.llm.invoke(prompt)
        return response.content

    def run(self, query: str) -> dict:
        decision = self.choose_tool(query)

        tool_name = decision.get("tool", "none")
        tool_input = decision.get("tool_input", "")

        tool_result = self.run_tool(tool_name, tool_input)

        answer = self.final_answer(
            query=query,
            tool=tool_name,
            tool_result=tool_result
        )

        return {
            "query": query,
            "tool_decision": decision,
            "tool_result": tool_result,
            "answer": answer
        }