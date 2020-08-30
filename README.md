# MapleBossLogger

[![Build Status](https://travis-ci.org/retore404/maple_boss_logger.svg?branch=develop)](https://travis-ci.org/retore404/maple_boss_logger)
![test](https://github.com/retore404/maple_boss_logger/workflows/test/badge.svg)

# DB関連初期構築について

- docker-compose run web python manage.py makemigrations
- docker-compose run web python manage.py migrate
- docker-compose run web python manage.py createsuperuser
- docker-compose run web python manage.py loaddata boss.json --app logger



