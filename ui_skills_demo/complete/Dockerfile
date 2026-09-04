FROM python:3.11-slim

WORKDIR /app

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制测试代码
RUN mkdir -p /app/ui_skills_demo/complete
COPY . /app/ui_skills_demo/complete/

ENV PYTHONPATH=/app

# 默认命令
CMD ["pytest", "ui_skills_demo/complete/test_cases", "-v", "--alluredir=allure-results"]