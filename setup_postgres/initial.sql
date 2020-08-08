CREATE DATABASE maple_boss_logger;
CREATE USER django WITH PASSWORD 'password';
ALTER ROLE django SET client_encoding TO 'utf8';
ALTER ROLE django SET default_transaction_isolation TO 'read committed';
ALTER ROLE django SET timezone TO 'Asia/Tokyo';
ALTER USER django CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE maple_boss_logger TO django;