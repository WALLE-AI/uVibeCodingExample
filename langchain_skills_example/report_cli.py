import os
import sys
from weekly_report_skill_example.agent import run_report_agent_example
from weekly_report_skill_example.skill_loader import load_report_skill
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

def get_agent():
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
    
    graph = create_agent(
        model=llm,
        tools=tools,
        system_prompt=(
            "你是一个全能的行政助理。你拥有专业的汇报技能。"
            "重要提示：在撰写任何报告之前，你必须使用 `load_report_skill` 工具"
            "来获取该报告类型的具体指令和格式。所有输出和生成的报告必须使用中文。"
        )
    )
    return graph

def main():
    print("=== AI 报告生成助手 ===")
    print("1. 生成日报 (Daily Report)")
    print("2. 生成周报 (Weekly Report)")
    choice = input("请选择 (1/2): ")

    graph = get_agent()

    if choice == "1":
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

    elif choice == "2":
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
