FROM python:3.10-slim

# Tạo thư mục app
WORKDIR /app

# Cài đặt dependencies
RUN pip install --no-cache-dir fastapi uvicorn sentence-transformers

# Copy source
COPY main.py /app/main.py

# Expose port
EXPOSE 8000

# Chạy server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
