FROM python:3.10
 
WORKDIR /app
COPY . .
 
RUN pip install -r requirements.txt \
    && pip install langchain==0.1.17 \
    && pip install huggingface-hub==0.23.4 \
    && pip install langchain-community
 
CMD ["python", "-u", "server.py"]