@echo off
echo ========================================
echo  今日头条自动发布工具 - 安装脚本
echo ========================================
echo.

REM 检查Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到Python，请先安装Python 3.8+
    pause
    exit /b 1
)

echo [1/3] 安装Python依赖...
pip install playwright

echo [2/3] 安装Chromium浏览器...
playwright install chromium

echo [3/3] 安装完成！
echo.
echo ========================================
echo  使用方法：
echo  1. 运行 python toutiao_publisher.py 测试
echo  2. 首次使用需要扫码登录
echo  3. 登录状态会自动保存
echo ========================================
pause
