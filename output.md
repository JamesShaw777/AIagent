# AIagent

这是一个供个人使用的 AIagent 仓库。

## 环境设置

### 创建虚拟环境
使用以下命令创建 Python 虚拟环境：
```bash
python3 -m venv venv
```

### 激活虚拟环境
激活虚拟环境：
```bash
source venv/bin/activate
```

## 安装依赖

### 安装 OpenAI 库
在激活的虚拟环境中安装 OpenAI 库：
```bash
python3 -m pip install openai
```

## 配置 API 密钥

### 导出 API 密钥
需要将你的 API 密钥导出到环境变量中：
```bash
export API_KEY="your_api_key_here"
```

### 提供商说明
- 我使用阿里云作为提供商。
- 通常，API 结构是相同的，因此你无需进行任何更改。