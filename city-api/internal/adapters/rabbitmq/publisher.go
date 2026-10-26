package rabbitmq

import (
	"encoding/json"

	"city-api/internal/domain"

	amqp "github.com/rabbitmq/amqp091-go"
)

type Publisher struct {
	channel *amqp.Channel
}

func NewPublisher(channel *amqp.Channel) *Publisher {
	return &Publisher{channel: channel}
}

func (p *Publisher) Publish(Message domain.Message) error {
	body, err := json.Marshal(Message)
	if err != nil {
		return err
	}

	return p.channel.Publish(
		"",
		"tweek_messages",
		false,
		false,
		amqp.Publishing{
			ContentType: "application/json",
			Body:        body,
		},
	)
}
