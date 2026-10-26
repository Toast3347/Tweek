
FROM golang:1.27-alpine AS build

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 go build -o /city-api ./cmd/api

FROM alpine:3.22

COPY --from=build /city-api /city-api

EXPOSE 8080

CMD ["/city-api"]
