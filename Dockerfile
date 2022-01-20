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
    requests \
    uvicorn
RUN curl -fsSL https://get.deta.dev/cli.sh | sh
WORKDIR /api_predictions_bets
COPY ./api_predictions_bets .
CMD ["make", "run"]