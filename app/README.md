# SimpleTimeService (app)

A tiny FastAPI application that returns the current UTC timestamp and the visitor IP.

## Build locally

```bash
cd app
docker build -t simple-time-service .

## Run locally

docker run -p 8000:8000 simple-time-service
# then visit http://localhost:8000/

## API

GET / returns JSON:

{
  "timestamp": "2025-12-11T12:34:56.789Z",
  "ip": "172.17.0.1"
}
