from ingest import ingest_pdf
from query import ask_question
from vector_store import clear_vector_store


def menu():
    while True:
        print("\nDAY 3 ADVANCED RAG AGENT")
        print("1. Ingest PDF")
        print("2. Ask Question")
        print("3. Clear Vector DB")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":
            pdf_path = input("PDF path: ")
            chunks = ingest_pdf(pdf_path)
            print(f"Ingested {chunks} chunks")

        elif choice == "2":
            question = input("Question: ")
            result = ask_question(question)

            print("\nANSWER:\n")
            print(result.answer)

            print("\nCITATIONS:")
            for citation in result.citations:
                print(
                    f"- {citation.source}, page {citation.page}: "
                    f"{citation.chunk_preview}"
                )

        elif choice == "3":
            clear_vector_store()
            print("Vector database cleared.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()