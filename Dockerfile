FROM python:3-alpine
LABEL maintainer ="Pagar.me"
ARG FUNCTION_DIR="/src"
WORKDIR ${FUNCTION_DIR}
COPY ./src ${FUNCTION_DIR}
RUN apk add build-base zlib-dev jpeg-dev
RUN pip install xlrd Pillow Flask
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=5000
ENTRYPOINT ["flask", "run"]

