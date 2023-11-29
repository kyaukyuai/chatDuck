.PHONY: all
all: build

CONTAINER_NAME=duck-chat
IMAGE_NAME=$(CONTAINER_NAME)
PORT=8501

.PHONY: build
build:
	@echo "Building Docker image..."
	docker build -t $(IMAGE_NAME) .

.PHONY: run
run: build
	@echo "Running Docker container..."
	docker run -p $(PORT):$(PORT) $(IMAGE_NAME)

.PHONY: stop
stop:
	@echo "Stopping Docker container..."
	docker stop $(CONTAINER_NAME)

.PHONY: seed
seed:
	@echo "Creating seed data..."
	./seed.sh

.PHONY: setup
setup:
	@echo "Running setup..."
	./setup.sh
