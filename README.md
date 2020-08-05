# Postgres初期セットアップについて

初期構築時に以下の手順を実施する．

- docker-compose up -d 
- docker-compose ps
    - DBのコンテナ名を確認する
- docker exec -it <<コンテナ名>> bash
- psql
    - CREATE DATABASE maple_boss_logger;
    - CREATE USER django WITH PASSWORD 'password';
    - ALTER ROLE django SET client_encoding TO 'utf8';
    - ALTER ROLE django SET default_transaction_isolation TO 'read committed';
    - ALTER ROLE django SET timezone TO 'Asia/Tokyo';
    - GRANT ALL PRIVILEGES ON DATABASE maple_boss_logger TO django;
- docker-compose run web python manage.py makemigrations
- docker-compose run web python manage.py migrate
- docker-compose run web python manage.py createsuperuser
- docker-compose up

