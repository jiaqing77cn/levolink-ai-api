# Claude Code 接入教程

> 国内使用 Claude Code 的最佳方案，无需翻墙，低延迟。

## 什么是 Claude Code

Claude Code 是 Anthropic 官方推出的 AI 编程助手，可以直接在终端中使用，支持代码生成、重构、Bug 修复、测试编写等。

## 配置步骤

### 1. 安装 Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. 配置环境变量

```bash
# 添加到 ~/.bash_profile 或 ~/.zshrc
export ANTHROPIC_AUTH_TOKEN="你的 Levolink API Key"
export ANTHROPIC_BASE_URL="https://ai.levolink.com/v1"

# 生效
source ~/.bash_profile
```

### 3. 开始使用

```bash
cd your-project
claude
```

## 推荐分组

| 分组 | 倍率 | 适合场景 |
|------|------|---------|
| 默认(Azure+MJ) | 1.0x | 日常使用，性价比高 |
| CC 专属 | 2.4x | Claude Code 专项优化，稳定性最好 |
| anti/kiro | 1.2x | 性价比之选 |

## 常见问题

### Q: Claude Code 报错 "authentication failed"

检查环境变量是否正确设置：
```bash
echo $ANTHROPIC_AUTH_TOKEN
echo $ANTHROPIC_BASE_URL
```

### Q: 响应速度慢

尝试切换分组。CC 专属分组针对 Claude Code 做了优化，速度更快。

### Q: 支持 Claude Opus 4.8 吗

支持。在 Claude Code 中输入 `/model` 即可切换模型。

## 相关链接

- [Levolink AI 官网](https://ai.levolink.com)
- [Claude Code 官方文档](https://docs.anthropic.com/en/docs/claude-code)
- [API 文档](https://levolink.apifox.cn/)
