.PHONY: dev
dev:
	poetry install

.PHONY: build
build:
	poetry build

.PHONY: test
test:
	poetry run pytest	-v


# dev purposes only

# puppet cli task
puppet:
	poetry run exify puppet ./test_images/osprey.jpg
