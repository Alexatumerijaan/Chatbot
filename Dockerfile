# Use an official Python runtime as the base image
FROM python:3.8-alpine
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /Chatbot
COPY start.sh /start.sh
ENV PORT 5000
EXPOSE 5000
CMD ["/bin/bash", "/start.sh"]
