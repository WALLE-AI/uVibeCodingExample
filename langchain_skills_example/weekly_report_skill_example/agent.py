import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from weekly_report_skill_example.skill_loader import load_report_skill

# Load environment variables from .env
load_dotenv()

def run_report_agent_example(mode="build"):
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
    
    # Mode-specific instructions
    if mode == "plan":
        mode_instructions = (
            "你现在处于【规划模式】(PLAN MODE)。\n"
            "执行逻辑：\n"
            "1. 必须先调用 `load_report_skill(skill_name='planner')` 获取规划专家指令。\n"
            "2. 获取指令后，严格按照指令要求的【格式】和【准则】对用户的任务进行拆解，输出详细的待办事项清单 (To-Do List)。\n"
            "3. 严禁生成最终的报告正文，只输出规划方案。\n"
        )
    else:
        mode_instructions = (
            "你现在处于【执行模式】(BUILD MODE)。\n"
            "执行逻辑：\n"
            "1. 必须根据需求调用 `load_report_skill` 加载相应的报告技能（如 'daily_report' 或 'weekly_report'）。\n"
            "2. 获取指令后，直接生成高质量、专业的中文报告正文内容。\n"
        )

    # ReAct prompt template
    template = (
        "你是一个全能的行政助理。你拥有专业的汇报技能。\n"
        f"{mode_instructions}\n"
        "你可以使用以下工具：\n"
        "{tools}\n\n"
        "使用以下格式：\n"
        "Thought: 你应该总是思考接下来要做什么。\n"
        "Action: 要采取的操作，应该是 [{tool_names}] 之一。\n"
        "Action Input: 操作的输入（注意：只需提供技能名称字符串，不要使用 skill_name= 或引号，如：planner）。\n"
        "Observation: 操作的结果。\n"
        "...（这个 Thought/Action/Action Input/Observation 可以重复 N 次）\n"
        "Thought: 我现在知道最终答案了。\n"
        "Final Answer: 最终对用户的中文回复。\n\n"
        "注意：调用工具是获取指令的手段，你的最终目标是给出生成的中文内容。不要只停留于调用工具。\n\n"
        "User Input: {input}\n"
        "Thought: {agent_scratchpad}"
    )
    
    prompt = ChatPromptTemplate.from_template(template)

    # Using create_react_agent for robust tool calling
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
    
    # Example: Execute based on mode
    if mode == "plan":
        print("--- Mode: PLAN ---")
        user_input = "帮我写一份关于标注工具技术评审的日报。"
    else:
        print("--- Mode: BUILD ---")
        user_input = "帮我写一份日报。今日工作：修复了登录流程的 Bug，参与了 Sprint 计划会议，评审了 3 个 PR。"

    result = agent_executor.invoke({"input": user_input})
    print(result["output"])

    print("\n\n--- Example 2: Weekly Report (Build) ---")
    daily_summaries = """
    Mon: Finished API integration.
    Tue: Debugged performance issues.
    Wed: Mentored junior dev on React.
    Thu: Documentation for the SDK.
    Fri: Released beta version.
    """
    
    inputs2 = {"input": f"Please generate a weekly executive summary based on these daily summaries: {daily_summaries}", "chat_history": []}
    result2 = agent_executor.invoke(inputs2)
    print(result2["output"])

if __name__ == "__main__":
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "build"
    run_report_agent_example(mode=mode)
