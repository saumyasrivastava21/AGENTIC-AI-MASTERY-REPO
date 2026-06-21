from agents.research_agent import ResearchAgent


def print_response(response):
    print("\n" + "=" * 80)
    print("ROUTE:", response.route)
    print("CONFIDENCE:", response.confidence)
    print("REASON:", response.reason)

    print("\nTOOL INPUT:")
    print(response.tool_input)

    print("\nTOOL OUTPUT:")
    print(response.tool_output)

    print("\nFINAL ANSWER:")
    print(response.final_answer)
    print("=" * 80)


def main():
    agent = ResearchAgent()

    print("=" * 80)
    print("DAY 2 — LANGCHAIN STRUCTURED ROUTER AGENT")
    print("Type 'exit' to stop")
    print("=" * 80)

    while True:
        query = input("\nYou: ")

        if query.lower() in ["exit", "quit"]:
            print("Agent stopped.")
            break

        try:
            response = agent.run(query)
            print_response(response)

        except Exception as e:
            print(f"Agent error: {str(e)}")


if __name__ == "__main__":
    main()