# Tweek
South Park messaging system. Where Cartman can finally get some respect on his authoritah!!

# Setup

## RabbitMQ (Queue)
Start Docker and run the following command to set up rabbitmq

```
docker run -d --name rabbitmq `
  -p 5672:5672 `
  -p 15672:15672 `
  rabbitmq:4-management
```

RabbitMQ endpoints:

- AMQP: localhost:5672

- Management UI: http://localhost:15672

## Go (API)

Open a terminal in the city-api directory.

### Install dependencies using

```
go mod download
```

### Run Go API

```
go run ./cmd/api
```

### API
#### Listens on

```
http://localhost:8080
```

#### Expects
JSON
```json
{
  "author":"Cartman",
  "body":"Respect my authoritah!"
}
```

## Python (Consumer)

Open a separate terminal in the city-consumer directory.

### Create a virtual environment

```
python -m venv .venv
```

### Activate virtual environment

#### Windows PowerShell:
```
.\.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt:
```
.venv\Scripts\activate.bat
```

#### macOS/Linux:
```
source .venv/bin/activate
```

### Install dependencies

Run:
```
python -m pip install -r requirements.txt
```

### Run the consumer
```
python city_consumer.py
```

## Send messages

Send a POST message to:
```
http://localhost:8080/messages
```

With the following JSON:
```json
{
  "author":"Stan",
  "body":"Oh my god, they killed kenny!"
}
```

# Finally 

Kanye likes fish sticks!