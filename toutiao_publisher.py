#!/usr/bin/env python3
"""
今日头条自动发布脚本
基于 Playwright + Chrome
"""

import asyncio
from playwright.async_api import async_playwright
from datetime import datetime
import json

class ToutiaoPublisher:
    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None
        
    async def init_browser(self, headless=False):
        """初始化浏览器"""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=headless,
            args=['--disable-blink-features=AutomationControlled']
        )
        self.context = await self.browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        self.page = await self.context.new_page()
        
    async def login(self, phone=None, password=None):
        """登录今日头条"""
        print("[1/5] 打开登录页面...")
        await self.page.goto('https://sso.toutiao.com/login/')
        await asyncio.sleep(2)
        
        # 等待登录框加载
        print("[2/5] 等待扫码/短信登录...")
        print("请在浏览器中完成登录（扫码或短信验证）")
        
        # 等待跳转到后台（说明登录成功）
        await self.page.wait_for_url('https://mp.toutiao.com/**', timeout=120000)
        print("[3/5] 登录成功！")
        
        # 保存登录状态
        await self.context.storage_state(path='toutiao_auth.json')
        
    async def publish_article(self, title, content, cover_image=None):
        """发布文章"""
        print("[4/5] 打开发布页面...")
        
        # 点击发布按钮
        await self.page.goto('https://mp.toutiao.com/profile_v4/graphic/publish')
        await asyncio.sleep(3)
        
        # 填写标题
        print("填写标题...")
        title_input = await self.page.wait_for_selector('input[placeholder*="标题"], textarea[placeholder*="标题"], [data-testid="title-input"], input[maxlength="50"]', timeout=10000)
        await title_input.fill(title)
        
        # 填写内容
        print("填写内容...")
        # 尝试找到富文本编辑器
        content_editor = await self.page.wait_for_selector('[contenteditable="true"], .ProseMirror, #editor, .editor-content', timeout=10000)
        await content_editor.click()
        await content_editor.fill(content)
        
        # 上传封面（如果有）
        if cover_image:
            print("上传封面...")
            # 找到封面上传按钮
            upload_btn = await self.page.query_selector('input[type="file"], .upload-btn, [data-testid="cover-upload"]')
            if upload_btn:
                await upload_btn.set_input_files(cover_image)
                await asyncio.sleep(2)
        
        # 发布
        print("[5/5] 发布文章...")
        publish_btn = await self.page.wait_for_selector('button:has-text("发布"), button:has-text("立即发布"), [data-testid="publish-btn"]', timeout=10000)
        await publish_btn.click()
        
        # 等待发布成功提示
        await asyncio.sleep(3)
        print("✅ 文章发布成功！")
        
    async def close(self):
        """关闭浏览器"""
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
            
    async def run(self, title, content, cover_image=None, phone=None, password=None):
        """完整流程"""
        try:
            await self.init_browser(headless=False)
            
            # 尝试加载已保存的登录状态
            try:
                with open('toutiao_auth.json', 'r') as f:
                    await self.context.add_cookies(json.load(f)['cookies'])
                print("使用已保存的登录状态")
            except:
                await self.login(phone, password)
            
            await self.publish_article(title, content, cover_image)
            
        except Exception as e:
            print(f"❌ 错误: {e}")
            raise
        finally:
            await self.close()


async def main():
    """测试发布"""
    publisher = ToutiaoPublisher()
    
    title = "测试文章 - " + datetime.now().strftime("%Y-%m-%d %H:%M")
    content = """
这是一篇测试文章。

今日头条自动发布功能测试。

测试时间：{time}
    """.format(time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    await publisher.run(title=title, content=content)


if __name__ == "__main__":
    asyncio.run(main())
