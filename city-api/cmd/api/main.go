package main

import (
	"log"
	"net/http"

	httpadapter "city-api/internal/adapters/http"
	"city-api/internal/adapters/rabbitmq"
	"city-api/internal/service"

	amqp "github.com/rabbitmq/amqp091-go"
)

func main() {
	connection, err := amqp.Dial("amqp://guest:guest@localhost:5672/")
	if err != nil {
		log.Fatal("Failed to connect to RabbitMQ:", err)
	}
	defer connection.Close()

	channel, err := connection.Channel()
	if err != nil {
		log.Fatal("Failed to open RabbitMQ channel:", err)
	}
	defer channel.Close()

	_, err = channel.QueueDeclare(
		"tweek_messages",
		true,
		false,
		false,
		false,
		nil,
	)
	if err != nil {
		log.Fatal("Failed to declare queue:", err)
	}

	publisher := rabbitmq.NewPublisher(channel)
	messageService := service.NewMessageService(publisher)
	handler := httpadapter.NewMessageHandler(messageService)

	http.HandleFunc("POST /messages", handler.CreateMessage)

	log.Println("API listening on :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
