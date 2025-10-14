# Auto-Demo（test-clean 稳定版）

![CI](https://github.com/joy206/auto-demo/actions/workflows/ci.yml/badge.svg)

最小可运行集合 · Selenium + pytest

## 一键本地跑
```bash
pip install -r requirements.txt
pytest tests/ui -v
```

## 最新结果
✅ CI 绿色打勾，pytest通过

## 技术栈
| 技术     | 版本   |
|----------|--------|
| Python   | 3.11   |
| pytest   | 8.4.1  |
| selenium | 4.35.0 |

## 目录
```
tests/ui/
├── conftest.py          # function级，每条用例自动分配新浏览器
├── simple_test_project/ # 简单业务用例
│   └── test_*.py        
requirements.txt         # 一键安装依赖
.github/workflows/ci.yml # 云跑配置
```

## 更多运行方式
- 无头（默认，与CI一致）
- 有头（本地想看界面）
  ```bash
  HEAD=0 pytest tests/ui -v
  ```

## 驱动逻辑
| 场景                     | 驱动                                                         |
|--------------------|---------------------------------------------|
| 本地已有驱动        | 自动使用drivers/ 目录下对应平台文件       |
| 无驱动/版本不符合| 自动通过webdriver-manager下载并缓存  |

