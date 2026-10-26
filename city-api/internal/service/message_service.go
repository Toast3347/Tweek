package service

import (
	"city-api/internal/domain"
	"city-api/internal/ports"
)

type MessageService struct {
	publisher ports.MessagePublisher
}

func NewMessageService(publisher ports.MessagePublisher) *MessageService {
	return &MessageService{publisher: publisher}
}

func (s *MessageService) Send(message domain.Message) error {
	return s.publisher.Publish(message)
}
