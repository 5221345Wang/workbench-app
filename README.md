# 今日头条自动发布工具

基于 Playwright + Chrome 的自动化发布脚本。

## 功能

- ✅ 自动登录（支持扫码/短信验证）
- ✅ 文章发布
- ✅ 封面上传
- ✅ 登录状态保存（免重复登录）

## 安装

```bash
# 安装依赖
pip install playwright
playwright install chromium
```

## 使用

### 1. 首次使用（需要登录）

```python
from toutiao_publisher import ToutiaoPublisher
import asyncio

async def main():
    publisher = ToutiaoPublisher()
    
    await publisher.run(
        title="文章标题",
        content="文章内容...",
        cover_image="cover.jpg"  # 可选
    )

asyncio.run(main())
```

运行后会弹出浏览器，你需要：
1. 扫码或短信验证登录
2. 登录成功后自动保存状态

### 2. 后续使用（免登录）

登录状态会自动保存到 `toutiao_auth.json`，后续直接运行即可。

### 3. 集成到工作流

```python
# daily_publish.py - 每日自动发布
import asyncio
from toutiao_publisher import ToutiaoPublisher

async def publish_daily(title, content):
    publisher = ToutiaoPublisher()
    await publisher.run(title=title, content=content)

if __name__ == "__main__":
    asyncio.run(publish_daily(
        title="今日热点分析",
        content="..."
    ))
```

## 注意事项

1. **首次登录**：需要人工完成扫码/短信验证
2. **登录状态**：有效期约7-30天，过期需重新登录
3. **频率限制**：建议每天不超过5篇文章，避免被封
4. **IP限制**：频繁操作可能触发验证码

## 文件结构

```
toutiao-publisher/
├── toutiao_publisher.py    # 主程序
├── toutiao_auth.json       # 登录状态（自动生成）
├── README.md               # 说明文档
└── examples/               # 示例脚本
    └── daily_publish.py    # 每日发布示例
```

## 依赖

- Python 3.8+
- playwright
- chromium

## 免责声明

本工具仅供学习研究使用，请遵守今日头条平台规则，合理使用自动化工具。
