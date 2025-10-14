# Auto-Demo （main 开发分支）

** 此分支为日常开发分支**，CI可能处于失败状态，仅供迭代使用。
** 稳定运行版本**请切换到
[![CI](https://github.com/oy206/auto-demo/actions/workflows/ci.yml/badge.svg?branch=test-clean)](https://github.com/joy206/auto-demo/tree/test-clean)

## 一键本地跑
```bash
pip install -r requirements.txt
pytest tests/ui -v
```

## 技术栈
| 技术     | 版本   |
|----------|--------|
| Python   | 3.11   |
| pytest   | 8.4.1  |
| selenium | 4.35.0 |

## 目录（补充中）
tests/ui/
├── conftest.py          # 会话级浏览器
├── simple_test_project/ # 简单业务用例
│   └── test_*.py
├── base_page_project/   # PO 模式业务用例
requirements.txt         # 一键安装依赖
.github/workflows/ci.yml # 云跑配置
