package http

import (
	"encoding/json"
	"net/http"

	"city-api/internal/domain"
	"city-api/internal/service"
)

type MessageHandler struct {
	service *service.MessageService
}

func NewMessageHandler(service *service.MessageService) *MessageHandler {
	return &MessageHandler{service: service}
}

func (h *MessageHandler) CreateMessage(w http.ResponseWriter, r *http.Request) {
	var message domain.Message

	if err := json.NewDecoder(r.Body).Decode(&message); err != nil {
		http.Error(w, "Invalid JSON", http.StatusBadRequest)
		return
	}

	if message.Author == "" || message.Body == "" {
		http.Error(w, "author and body are required", http.StatusBadRequest)
		return
	}

	if err := h.service.Send(message); err != nil {
		http.Error(w, "Failed to publish message", http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusAccepted)
	json.NewEncoder(w).Encode(map[string]string{
		"status": "Your city message has been successfully published",
	})
}
