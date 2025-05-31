FROM python:3.9-slim

WORKDIR /app

COPY final_task/requirements.txt /app/requirements.txt
RUN test -f /app/requirements.txt || (echo "requirements.txt не найден" && exit 1)
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY final_task/model.pkl /app/model.pkl
COPY final_task/api.py /app/api.py

RUN test -f /app/model.pkl || (echo "model.pkl не найден" && exit 1)
RUN test -f /app/api.py || (echo "api.py не найден" && exit 1)

EXPOSE 8000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]