# Используем базовый образ Python
FROM python:3.9-slim



CMD ["python", "-c", "import time\nwhile True: time.sleep(10)"]