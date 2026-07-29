# Claude Desktop 接入教程

> 在 Claude Desktop 桌面应用中使用 Levolink AI，无需翻墙直接调用 Claude 模型。

## 什么是 Claude Desktop

Claude Desktop 是 Anthropic 官方推出的桌面客户端，支持 macOS 和 Windows。通过配置环境变量，可以让 Claude Desktop 通过 Levolink AI 中转访问 Claude 模型。

## 配置步骤

### 1. 设置环境变量

**macOS：**

```bash
# 添加到 ~/.zshrc 或 ~/.bash_profile
export ANTHROPIC_API_KEY="你的 Levolink API Key"
export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"

# 生效
source ~/.zshrc
```

**Windows：**

```powershell
# PowerShell 永久设置
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "你的Key", "User")
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://ai.levolink.com/v1", "User")
```

### 2. 重启 Claude Desktop

完全退出 Claude Desktop（不是最小化），然后重新启动。应用会读取新的环境变量。

### 3. 验证连接

在 Claude Desktop 中发送一条消息，如果能正常收到回复，说明已通过 Levolink AI 中转成功。

## MCP Server 配置

Claude Desktop 支持 MCP（Model Context Protocol），可以接入更多工具：

编辑配置文件：
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "levolink": {
      "command": "curl",
      "args": ["https://ai.levolink.com/v1/chat/completions"]
    }
  }
}
```

## 推荐模型

| 用途 | 模型 | 分组建议 |
|------|------|---------|
| 日常对话 | `claude-sonnet-4-6` | 默认 (1.0x) |
| 复杂任务 | `claude-opus-4-8` | 默认 (1.0x) |
| 轻量任务 | `claude-haiku-4-5` | 默认 (1.0x) |

## 常见问题

### Q: Claude Desktop 启动后没有读取环境变量？

确保完全退出应用（右键托盘图标 -> Quit），然后从终端启动：

```bash
open -a "Claude"
```

### Q: 提示 "connection error"？

检查 API Key 是否正确，Base URL 是否以 `/v1` 结尾。

### Q: 支持 Claude Opus 4.8 吗？

支持。在对话中输入 `/model claude-opus-4-8` 切换模型。

## 相关链接

- [Levolink AI 官网](https://ai.levolink.com)
- [Claude Desktop 官方下载](https://claude.ai/download)
- [API 文档](https://levolink.apifox.cn/)
