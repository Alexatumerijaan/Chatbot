COPY . /app/
WORKDIR /app/
RUN pip3 install -U -r requirements.txt
CMD bash start
