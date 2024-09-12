FROM ghcr.io/mlflow/mlflow:v2.16.0
# install curl
RUN apt-get update && apt-get install -y curl

ENTRYPOINT ["mlflow", "ui", "--host", "0.0.0.0"]

