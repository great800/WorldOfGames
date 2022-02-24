FROM python:3-alpine
WORKDIR /Dock
RUN python --version
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY Scores.txt /Dock/Scores.txt
COPY . .
CMD ["python", "-u", "MainScores.py"]




