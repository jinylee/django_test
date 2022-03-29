# 실제 타켓이름과 해당 경로내에 파일 혹은 디렉토리 이름과 중복이 있을 경우 설정하여 타켓임을 선언함
.PHONY: test help default

# default task 설정
default: test

# help task 설정
help:
	@echo 'Management commands for test django:'
	@echo
	@echo 'Usage:'
	@echo '    make up ENV="env"     	Run specific local Server(dev-based or stand-alone).'
	@echo '    make down ENV="env"     	Down specific local Server(dev-based or stand-alone).'
	@echo '    make build            	Build Docker image.'
	@echo


up:
ifndef ENV
	@echo 'env: local'
	docker-compose -f compose/local.yml up &
else
	@echo 'env: $(ENV)'
	docker-compose -f compose/$$ENV.yml up &
endif

down:
ifndef ENV
	@echo 'env: local'
	docker-compose -f compose/local.yml down &
else
	@echo 'env: $(ENV)'
	docker-compose -f compose/$$ENV.yml down &
endif

# Use double dollar sign for escaping dollar sign
#env $$(./docker_env_to_shell_env.sh .envs/local_django_env | xargs) python manage.py $$CMD
run:
ifndef ENV
	@echo 'env: local'
	python manage.py runserver --settings=mysite.settings.local 0.0.0.0:8000
else
	@echo 'env: $(ENV)'
	python manage.py runserver --settings=mysite.settings.$$ENV
endif


build:
ifndef ENV
	@echo 'env: local'
	docker-compose -f compose/local.yml build --force-rm app
else
	@echo 'env: $(ENV)'
	docker-compose -f compose/$$ENV.yml build --force-rm app
endif

clean-pycache:
	find . -name *.pyc -type f -delete

clean: clean-pycache down
