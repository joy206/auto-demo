# Auto-Demo



基于 Selenium + Pytest 的 Swag Labs UI 自动化测试练习项目，支持 Docker 容器化运行，集成 GitHub Actions 持续集成。



---



## 查看测试报告



每次推送 main 分支后，Allure 测试报告会自动部署到 GitHub Pages：



https://joy206.github.io/auto-demo/



---



## 获取 Docker 镜像



CI 自动构建的镜像已推送到 GitHub Container Registry：



https://github.com/joy206/auto-demo/pkgs/container/swaglabs-tester



## 拉取最新镜像

docker pull ghcr.io/joy206/swaglabs-tester:latest



## 运行测试（需要连接 Selenium Grid）

docker run --rm -e SELENIUM\_REMOTE\_URL=http://your-grid:4444/wd/hub ghcr.io/joy206/swaglabs-tester:latest





## CI/CD 流水线



每次推送代码到 main 分支，GitHub Actions 自动：



1. 启动 Selenium Grid

2. 运行测试用例

3. 生成 Allure 报告 → 部署到 GitHub Pages

4. 构建 Docker 镜像 → 推送到 ghcr.io





## 项目结构



.

├── pages/              # Page Object 页面对象

├── test_cases/         # 测试用例

├── utils/              # 工具函数（日志、驱动）

├── locators/           # 元素定位器

├── drivers/            # 浏览器驱动

├── .github/

│   └── workflows/

│       └── ci-docker.yml      # GitHub Actions CI 配置

├── Dockerfile          # 镜像构建文件

├── docker-compose.yml  # 本地 Docker 编排

├── requirements.txt    # 依赖

└── pytest.ini          # pytest 配置





## 技术栈



- Python 3.11

- pytest 8.4.1

- Selenium 4.35.0

- Docker 最新

- Allure 2.x

