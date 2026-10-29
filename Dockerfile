FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
COPY . .
RUN useradd --create-home appuser && mkdir -p /app/app/data && chown -R appuser:appuser /app
USER appuser
EXPOSE 8501 8000
