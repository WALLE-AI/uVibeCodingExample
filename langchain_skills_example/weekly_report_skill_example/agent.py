import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from weekly_report_skill_example.skill_loader import load_report_skill

# Load environment variables from .env
load_dotenv()

def run_report_agent_example():
    # LLM configuration from environment variables
    api_base = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    api_key = os.getenv("OPENAI_API_KEY", "EMPTY")
    model_name = os.getenv("MODEL_NAME", "qwen3")
    
    llm = ChatOpenAI(
        model=model_name,
        openai_api_base=api_base,
        openai_api_key=api_key,
        temperature=0
    )
    
    tools = [load_report_skill]
    
    # Using the modern create_agent interface as per LangChain 1.2.7 docs
    graph = create_agent(
        model=llm,
        tools=tools,
        system_prompt=(
            "你是一个全能的行政助理。你拥有专业的汇报技能。"
            "重要提示：在撰写任何报告之前，你必须使用 `load_report_skill` 工具"
            "来获取该报告类型的具体指令和格式。所有输出和生成的报告必须使用中文。"
            "在未加载技能之前，请勿尝试撰写报告。"
        )
    )
    
    # Example 1: Daily Report
    print("--- Example 1: Daily Report ---")
    activities = """
    - Fixed bug in login flow
    - Attended sprint planning
    - Reviewed 3 pull requests
    - Started working on the new dashboard UI
    """
    
    inputs1 = {"messages": [{"role": "user", "content": f"Please write a daily report for today based on these activities: {activities}"}]}
    result1 = graph.invoke(inputs1)
    # create_agent returns the full list of messages in the "messages" key
    # The last message should be the assistant's response
    print(result1["messages"][-1].content)
    
    print("\n\n--- Example 2: Weekly Report ---")
    daily_summaries = """
    Mon: Finished API integration.
    Tue: Debugged performance issues.
    Wed: Mentored junior dev on React.
    Thu: Documentation for the SDK.
    Fri: Released beta version.
    """
    
    inputs2 = {"messages": [{"role": "user", "content": f"Please generate a weekly executive summary based on these daily summaries: {daily_summaries}"}]}
    result2 = graph.invoke(inputs2)
    print(result2["messages"][-1].content)

if __name__ == "__main__":
    run_report_agent_example()
