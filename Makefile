#!/usr/bin/env bash

COMPOSE_FILE?=local.yml
DOCKER_FILE=compose/local/django/Dockerfile
REPO=shevchenkoigor/app
TAG?=latest

up:
	docker-compose -f ${COMPOSE_FILE} up

up_hard:
	export COMPOSE_FILE=${COMPOSE_FILE} \
	&& docker-compose stop \
	&& docker-compose rm -f \
	&& docker image rm -f ${REPO}:${TAG} \
	&& docker build -t ${REPO}:${TAG} -f ${DOCKER_FILE} . \
	&& docker-compose up --build

ipython:
	docker-compose -f ${COMPOSE_FILE} run --rm django ipython

ipython_exec:
	docker-compose -f ${COMPOSE_FILE} exec django ipython

django_bash_exec:
	docker-compose -f ${COMPOSE_FILE} exec django sh

commit:
	git remote show origin && \
	git add . && \
	git commit -m '${COMMIT_MESSAGE}' && \
	git push  && \
	git branch --set-upstream-to=origin/`git rev-parse --abbrev-ref HEAD` `git rev-parse --abbrev-ref HEAD` && \
	docker build -t ${REPO}:${TAG} -f ${DOCKER_FILE} . && \
	docker push ${REPO}:${TAG}

user_admin:
	docker-compose -f ${COMPOSE_FILE} run --rm django python manage.py createsuperuser --email admin@example.com --username admin

