FROM python:3.10.13-slim

# 安装 Python 和必要的工具，合并RUN指令
RUN apt-get update && apt-get install -y xvfb wget \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt install -y xdg-utils libxrandr2 libxkbcommon0 libxdamage1 libasound2 fonts-liberation \
    libcurl3-gnutls libgbm1 libnspr4 libnss3 libu2f-udev libvulkan1 \
    libatk-bridge2.0-0  libatk1.0-0 libatspi2.0-0 libcairo2 libcups2 libgtk-3-0 libpango-1.0-0 \
    && dpkg -i google-chrome-stable_current_amd64.deb \
    && pip install DrissionPage==4.0.0b20 flask \
    && rm -rf /var/lib/apt/lists/* /google-chrome-stable_current_amd64.deb

# 添加和复制文件
COPY ./systemctl3.py /usr/bin/systemctl
ADD app.py /
ADD start.sh /

ENV PYTHONUNBUFFERED=1

CMD ["./start.sh"]
