FROM python:3
RUN pip install flask
ADD . /
ENV FLASK_APP server.py
CMD [ "python", "-m", "flask", "run" ]
