.PHONY:			up down rm re

up:
	sudo docker-compose build
	sudo docker-compose up

ps:
	sudo docker ps


down:
	sudo docker-compose down


rm: down
	sudo docker-compose rm -a

re:
	rm up