psql -c 'CREATE DATABASE maple_boss_logger' -U postgres
psql -c 'CREATE USER django WITH PASSWORD "password"' -U postgres
psql -c 'ALTER ROLE django SET client_encoding TO "utf8"' -U postgres
psql -c 'ALTER ROLE django SET default_transaction_isolation TO "read committed"' -U postgres
psql -c 'ALTER ROLE django SET timezone TO "Asia/Tokyo"' -U postgres
psql -c 'ALTER USER django CREATEDB' -U postgres
psql -c 'GRANT ALL PRIVILEGES ON DATABASE maple_boss_logger TO django' -U postgres