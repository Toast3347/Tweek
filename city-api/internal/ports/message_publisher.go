package ports

import "city-api/internal/domain"

type MessagePublisher interface {
	Publish(Message domain.Message) error
}
