FROM docker.io/library/alpine:3.24 as Base

COPY . /app
WORKDIR /app

RUN apk add --no-cache uvicorn uv

RUN uv sync

FROM Base

CMD ["uv", "run", "kekschen"]