all: run

run:
	docker-compose run --rm --service-ports  plone


build:
	docker-compose build plone


shell:
	docker-compose run --rm --service-ports  plone /bin/bash


.PHONY: run shell
