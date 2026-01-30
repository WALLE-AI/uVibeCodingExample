from weekly_report_skill_example.agent import run_report_agent_example

if __name__ == "__main__":
    try:
        run_report_agent_example()
    except Exception as e:
        print(f"Error running example: {e}")
        print("Note: This example requires an OPENAI_API_KEY environment variable and the 'langchain-openai' package.")
