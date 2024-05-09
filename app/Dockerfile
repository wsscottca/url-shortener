FROM python:3.12.2
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./ /app/app
EXPOSE 8000
ENTRYPOINT ["python", "-m"]
CMD ["uvicorn", "app.main:app","--host", "0.0.0.0", "--port", "8000"]