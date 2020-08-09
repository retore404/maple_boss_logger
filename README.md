# MapleBossLogger

[![Build Status](https://travis-ci.org/retore404/maple_boss_logger.svg?branch=develop)](https://travis-ci.org/retore404/maple_boss_logger)
![test](https://github.com/retore404/maple_boss_logger/workflows/test/badge.svg)

# マスタデータの初期構築について

DB初期セットアップ実施後に以下のコマンドでマスタデータのインポートが可能．

- docker-compose run web python manage.py loaddata boss.json --app logger



