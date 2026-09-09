# Auto-Demo

![CI Docker](https://github.com/joy206/auto-demo/actions/workflows/ci-docker.yml/badge.svg)


基于 Selenium + Pytest 的 Swag Labs UI 自动化测试练习项目，支持 Docker 容器化运行，集成 GitHub Actions 持续集成。
目录设置的比较多，要查看代码，请点击进入 ui\_skills\_demo/complete 目录。



## 查看测试报告



每次推送 main 分支后，Allure 测试报告会自动部署到 GitHub Pages：



https://joy206.github.io/auto-demo/



## 获取 Docker 镜像



CI 自动构建的镜像已推送到 GitHub Container Registry：



https://github.com/joy206/auto-demo/pkgs/container/swaglabs-tester



## 一键启动测试环境（自动拉取镜像）



docker compose -f ui_skills_demo/complete/docker-compose.yml up -d selenium-hub chrome-node



## 运行测试



docker compose -f ui_skills_demo/complete/docker-compose.yml run --rm tester



## CI/CD 流水线



每次推送代码到 main 分支，GitHub Actions 自动：



1. 启动 Selenium Grid
2. 运行测试用例
3. 生成 Allure 报告 → 部署到 GitHub Pages
4. 构建 Docker 镜像 → 推送到 ghcr.io





## 项目结构



.

├── pages/              # Page Object 页面对象

├── test\_cases/         # 测试用例

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



* Python 3.11
* pytest 8.4.1
* Selenium 4.35.0
* Docker 最新
* Allure 2.x

