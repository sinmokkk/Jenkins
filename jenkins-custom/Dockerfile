# 使用 Jenkins 官方 LTS 映像作為基礎映像
FROM jenkins/jenkins:lts

# 切換到 root 用戶，允許安裝系統依賴
USER root

# 更新 apt 包並安裝 Python 和必要工具
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && apt-get clean

# 創建虛擬環境
RUN python3 -m venv /opt/venv

# 確保使用虛擬環境的 pip 安裝 Python 依賴
RUN /opt/venv/bin/pip install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN /opt/venv/bin/pip install -r /tmp/requirements.txt

# 切換回 Jenkins 用戶
USER jenkins

# 配置環境變量，使得 Python 和 pip 使用虛擬環境中的版本
ENV PATH="/opt/venv/bin:$PATH"
