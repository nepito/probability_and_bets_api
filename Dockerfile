FROM python:3.8
RUN pip install \
    black \
    codecov \
    fastapi \
    flake8 \
    mutmut \
    pandas \
    pylint \
    pytest \
    pytest-cov \
    requests
RUN curl -fsSL https://get.deta.dev/cli.sh | sh
WORKDIR /app
COPY ./app .
CMD ["make", "run"]