all: run

.PHONY: clean build push run

clean:
	rm --force --recursive app/__pycache__
	rm --force --recursive app/tests/__pycache__

build:
	docker build --tag nepolin/api_predictions .

push: build
	docker push nepolin/api_predictions:latest

run: build
	docker run --rm --detach --name predictions --publish 80:80 nepolin/api_predictions