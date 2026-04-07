#!/usr/bin/env python3
"""
每日自动发布示例
可以配合定时任务（如Windows任务计划程序）使用
"""

import asyncio
import sys
sys.path.append('..')

from toutiao_publisher import ToutiaoPublisher
from datetime import datetime

async def publish_daily_article():
    """发布每日文章"""
    
    # 生成标题和内容（这里可以从你的内容生成系统获取）
    today = datetime.now().strftime("%Y年%m月%d日")
    
    title = f"【每日热点】{today}重要资讯汇总"
    
    content = f"""
<h1>今日热点资讯</h1>

<p>大家好，今天是{today}，为您带来今日重要资讯。</p>

<h2>一、科技动态</h2>
<p>（此处插入科技新闻内容）</p>

<h2>二、财经要闻</h2>
<p>（此处插入财经新闻内容）</p>

<h2>三、社会热点</h2>
<p>（此处插入社会热点内容）</p>

<hr>

<p><strong>免责声明：</strong>本文内容仅供参考，不构成任何投资建议。</p>

<p><strong>关注我，获取更多资讯！</strong></p>
    """
    
    publisher = ToutiaoPublisher()
    
    try:
        await publisher.run(
            title=title,
            content=content,
            cover_image=None  # 如果有封面图，填写路径
        )
        print(f"✅ {today} 文章发布成功！")
    except Exception as e:
        print(f"❌ 发布失败: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(publish_daily_article())
