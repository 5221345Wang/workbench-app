# 副总工作台APP开发文档

> 项目时间：2026年4月7日
> 开发人员：副总（AI助手）
> 技术栈：HTML5 + CSS3 + JavaScript + PWA

---

## 📱 项目概述

**项目名称**：副总工作台  
**项目类型**：PWA（渐进式Web应用）  
**访问地址**：https://5221345Wang.github.io/workbench-app  
**代码仓库**：https://github.com/5221345Wang/workbench-app

### 核心功能
- 📋 今日任务管理（可勾选完成）
- 📅 明日计划预览
- 🛠️ 技能库状态监控
- 🔑 API配置管理
- 👤 老板任务追踪（紧急/一般分类）

---

## 🎨 设计规范

### 视觉风格
- **主题**：深色科技风
- **主色调**：深蓝紫渐变背景
- **强调色**：
  - 蓝色 #00d4ff（任务）
  - 紫色 #a855f7（技能）
  - 粉色 #ec4899（紧急）
  - 绿色 #10b981（完成）
  - 橙色 #f59e0b（警告）

### 界面元素
- 玻璃拟态卡片（backdrop-filter）
- 动态渐变背景（浮动光球动画）
- 网格叠加纹理
- 呼吸灯状态指示

---

## 🏗️ 技术架构

### 文件结构
```
workbench-app/
├── index.html      # 主页面（单页应用）
├── data.json       # 数据源（实时同步）
├── manifest.json   # PWA配置
├── package.json    # 项目配置
└── sw.js          # Service Worker
```

### 核心技术
| 技术 | 用途 |
|------|------|
| HTML5 | 页面结构 |
| CSS3 | 样式+动画（Grid/Flex/Animation） |
| JavaScript | 交互逻辑+数据加载 |
| Fetch API | 实时数据获取 |
| GitHub Pages | 免费托管 |

---

## 📊 数据同步机制

### 同步流程
```
我修改 data.json
    ↓
git commit + push
    ↓
GitHub Pages 自动部署（约30秒）
    ↓
页面每30秒自动 fetch 最新数据
    ↓
用户看到更新内容
```

### 数据格式
```json
{
  "lastUpdated": "2026-04-07T17:25:00",
  "todayTasks": [...],
  "tomorrowTasks": [...],
  "bossTasks": [...],
  "skills": [...],
  "apis": [...]
}
```

---

## 🚀 部署步骤

### 1. 创建项目
```bash
mkdir workbench-app
cd workbench-app
```

### 2. 初始化Git
```bash
git init
git config user.name "副总工作台"
git config user.email "workbench@example.com"
```

### 3. 创建GitHub仓库
```bash
gh repo create workbench-app --public --source=. --remote=origin --push
```

### 4. 启用GitHub Pages
- 访问：https://github.com/用户名/workbench-app/settings/pages
- Source 选择 "Deploy from a branch"
- Branch 选择 "master" / "(root)"
- 点击 Save

### 5. 访问应用
等待1分钟后访问：https://用户名.github.io/workbench-app

---

## 📝 更新数据方法

### 添加新任务
1. 编辑 `data.json` 文件
2. 在对应数组中添加任务对象
3. 提交并推送：
```bash
git add data.json
git commit -m "添加新任务"
git push origin master
```

### 任务状态说明
| 状态 | 说明 |
|------|------|
| todo | 待开始 |
| doing | 进行中 |
| done | 已完成 |

### 优先级说明
| 优先级 | 颜色 |
|--------|------|
| high | 红色（紧急） |
| medium | 橙色（中等） |
| low | 绿色（一般） |

---

## 🎯 使用指南

### 手机安装
1. 手机浏览器打开访问地址
2. 点击菜单 → "添加到主屏幕"
3. 像原生APP一样使用

### 查看任务
- 首页显示统计概览
- 点击卡片进入详情页
- 任务可勾选完成

### 实时同步
- 页面每30秒自动刷新数据
- 无需手动刷新

---

## 🔧 维护说明

### 日常更新
- 每小时检查并更新任务状态
- 每日更新"今日任务"和"明日计划"
- 技能状态变更时及时更新

### 故障排查
| 问题 | 解决 |
|------|------|
| 页面不更新 | 检查GitHub Pages部署状态 |
| 数据不同步 | 强制刷新页面（Ctrl+F5） |
| 无法访问 | 检查网络或GitHub状态 |

---

## 📌 项目里程碑

| 时间 | 事件 |
|------|------|
| 2026-04-07 15:52 | 开始开发工作台APP |
| 2026-04-07 16:08 | 完成基础框架 |
| 2026-04-07 16:30 | 添加"需要我完成"板块 |
| 2026-04-07 17:01 | 完成UI美化 |
| 2026-04-07 17:18 | 部署到GitHub Pages |
| 2026-04-07 17:23 | 添加实时数据同步 |

---

## 💡 后续优化计划

- [ ] 添加数据持久化（后端API）
- [ ] 支持任务拖拽排序
- [ ] 添加数据统计图表
- [ ] 支持多用户协作
- [ ] 添加消息通知功能

---

**文档版本**：v1.0  
**最后更新**：2026-04-07  
**维护人员**：副总（AI助手）