import openai
import sys
import os

# --- 配置区域 ---
API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"  # 如果是国内镜像或DeepSeek，请替换此处
MODEL_NAME = "deepseek-v3.2"  # 或者使用 deepseek-chat, gpt-3.5-turbo 等
# ----------------

client = openai.OpenAI(api_key=API_KEY, base_url=BASE_URL)

def md_formatter_agent(user_input):
    system_prompt = (
        "你是一个专业的技术文档工程师。用户会输入一些技术片段、命令或草稿。\n"
        "你的任务：\n"
        "1. 整理为标准的 Markdown 格式。\n"
        "2. 识别其中的命令（如 gost, realm 命令），必须放入独立的 ```bash 代码块中。\n"
        "3. 识别其中的配置项，使用表格或列表展示。\n"
        "4. 保持技术参数的准确性，不要随意翻译命令中的参数。\n"
        "5. 使用 H2/H3 标题分段，使文档具有阅读美感。"
    )

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.3 # 降低随机性，保证技术参数准确
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"发生错误: {str(e)}"

if __name__ == "__main__":
    print("=== Markdown 技术文档格式化 Agent ===")
    print("【使用说明】")
    print("1. 直接粘贴你的内容（支持多行和特殊字符）。")
    print("2. 粘贴完成后：")
    print("   - Windows: 按回车后按 Ctrl+Z 再按回车")
    print("   - Mac/Linux: 按回车后按 Ctrl+D")
    print("---------------------------------------")

    # 使用 sys.stdin.read() 一次性读取所有输入，避免被特殊字符干扰
    try:
        raw_text = sys.stdin.read()
    except EOFError:
        pass

    if raw_text.strip():
        print("\n[正在转换中...]\n")
        formatted_md = md_formatter_agent(raw_text)
        
        print("\n" + "="*20 + " Markdown 源码 " + "="*20)
        print(formatted_md)
        print("="*55)
        
        # 可选：自动保存到文件
        with open("output.md", "w", encoding="utf-8") as f:
            f.write(formatted_md)
        print("\n已自动保存至 output.md")
    else:
        print("未检测到输入内容。")