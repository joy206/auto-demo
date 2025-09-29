# UI-Auto-Demo

![CI](https://github.com/lll/auto-demo/workflows/CI/badge.svg)

最小可运行集合 · Selenium + pytest · 数据驱动 · GitHub Actions 每日无头跑

## 一键本地跑
```bash
pip install -r requirements.txt
pytest tests/ui -v
```

## 最新结果
✅ CI 绿色打勾，pytest 100% 通过

## 技术栈
| 技术     | 版本   |
|----------|--------|
| Python   | 3.11   |
| pytest   | 8.4.1  |
| selenium | 4.35.0 |

## 目录
tests/ui/
├── conftest.py         # 会话级浏览器
├── simple_test_project/ # 简单业务用例
│   └── test_*.py
├── base_page_project/   # PO 模式业务用例
requirements.txt        # 一键安装依赖
.github/workflows/ci.yml # 云跑配置