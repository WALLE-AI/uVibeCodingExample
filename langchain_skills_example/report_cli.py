import os
import sys
from weekly_report_skill_example.agent import run_report_agent_example
from weekly_report_skill_example.skill_loader import load_report_skill
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def get_agent(mode="build"):
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
            "当前处于规划模式 (PLAN MODE)。你必须先使用 `load_report_skill` 加载 `planner` 技能。 "
            "你的任务是拆解任务并构建待办事项，绝对不要执行最终的生成操作。"
        )
    else:
        mode_instructions = (
            "当前处于执行模式 (BUILD MODE)。你必须使用 `load_report_skill` 加载相应的报告技能 (daily_report 或 weekly_report)。 "
            "你的任务是直接生成最终的报告内容。"
        )

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", (
            f"你是一个全能的行政助理。你拥有专业的汇报技能。 {mode_instructions} "
            "所有输出和生成的报告必须使用中文。"
        )),
        MessagesPlaceholder(variable_name="messages"),
    ])

    graph = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=prompt_template
    )
    return graph

def main():
    print("=== AI 报告生成助手 ===")
    print("1. 生成日报 (Daily Report)")
    print("2. 生成周报 (Weekly Report)")
    report_choice = input("请选择报告类型 (1/2): ")
    
    print("\n--- 选择操作模式 ---")
    print("p. 规划模式 (Plan Mode - 只构建任务和待办事项)")
    print("b. 执行模式 (Build Mode - 直接执行生成报告)")
    mode_choice = input("请选择模式 (p/b): ")
    mode = "plan" if mode_choice.lower() == "p" else "build"

    graph = get_agent(mode=mode)

    if report_choice == "1":
        print("\n请输入你今天的活动内容（输入 'EOF' 或连续按两次回车结束）:")
        lines = []
        while True:
            try:
                line = input()
                if line.strip().upper() == "EOF":
                    break
                # Optional: Allow empty line to terminate if it's the only way
                if not line.strip() and lines and not lines[-1].strip():
                    break
                lines.append(line)
            except EOFError:
                break
        content = "\n".join(lines)
        
        inputs = {"messages": [{"role": "user", "content": f"请为我写一份日报。以下是我的活动：\n{content}"}]}
        print("\n系统正在生成报告，请稍候...\n")
        result = graph.invoke(inputs)
        print("--- 你的日报 ---")
        print(result["messages"][-1].content)

    elif report_choice == "2":
        print("\n请输入本周的每日工作摘要（输入 'EOF' 或连续按两次回车结束）:")
        lines = []
        while True:
            try:
                line = input()
                if line.strip().upper() == "EOF":
                    break
                if not line.strip() and lines and not lines[-1].strip():
                    break
                lines.append(line)
            except EOFError:
                break
        content = "\n".join(lines)
        
        inputs = {"messages": [{"role": "user", "content": f"请为我生成本周的执行摘要。以下是我的每日记录：\n{content}"}]}
        print("\n系统正在生成报告，请稍候...\n")
        result = graph.invoke(inputs)
        print("--- 你的周报 ---")
        print(result["messages"][-1].content)
    else:
        print("无效选择。")

if __name__ == "__main__":
    main()
