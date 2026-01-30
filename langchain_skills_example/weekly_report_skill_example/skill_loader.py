import os
from langchain_core.tools import tool

def get_skill_content(skill_dir_name: str) -> str:
    """Reads the SKILL.md content from a skill directory."""
    # Assuming the skills folder is in the project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skill_path = os.path.join(base_dir, "skills", skill_dir_name, "SKILL.md")
    
    if os.path.exists(skill_path):
        with open(skill_path, "r", encoding="utf-8") as f:
            return f.read()
    return None

@tool
def load_report_skill(skill_name: str) -> str:
    """
    加载专业的报告技能指令。
    
    可用的技能：
    - daily-report: 将日报活动列表转换为专业中文日报。
    - weekly-report: 将日报汇总为执行级中文周报。
    
    返回技能的具体指令、格式和示例。
    """
    # Map input names to folder names if necessary
    mapping = {
        "daily_report": "daily-report",
        "weekly_report": "weekly-report",
        "daily-report": "daily-report",
        "weekly-report": "weekly-report"
    }
    
    folder_name = mapping.get(skill_name, skill_name)
    content = get_skill_content(folder_name)
    
    if content:
        return f"SUCCESS: 已加载 {folder_name} 技能。指令内容如下：\n\n{content}"
    else:
        return f"ERROR: 未找到技能 '{skill_name}'。请确保在 skills/ 目录下存在对应的文件夹和 SKILL.md 文件。"
