FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["file_metadata.py"]
ENTRYPOINT ["python3"]
