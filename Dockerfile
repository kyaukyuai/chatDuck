FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
  build-essential \
  curl \
  git \
  && rm -rf /var/lib/apt/lists/*

COPY . .

RUN make seed && make setup

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
