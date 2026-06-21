def summarizer_tool(text: str) -> str:
    words = text.split()

    if len(words) <= 40:
        return "Summary: " + text

    summary = " ".join(words[:40])
    return "Summary: " + summary + "..."