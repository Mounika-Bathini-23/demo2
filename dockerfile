FROM python:3.13-slim
WORKDIR /hi
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python" , "hi.py"]

