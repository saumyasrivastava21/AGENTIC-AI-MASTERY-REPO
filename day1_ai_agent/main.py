from agent import SimpleAIAgent


def main():
    agent = SimpleAIAgent()

    print("=" * 60)
    print("DAY 1 AI AGENT — Tool Calling CLI")
    print("Type 'exit' to stop")
    print("=" * 60)

    while True:
        query = input("\nYou: ")

        if query.lower() in ["exit", "quit"]:
            print("Agent stopped.")
            break

        result = agent.run(query)

        print("\nTool Decision:")
        print(result["tool_decision"])

        print("\nTool Result:")
        print(result["tool_result"])

        print("\nFinal Answer:")
        print(result["answer"])


if __name__ == "__main__":
    main()