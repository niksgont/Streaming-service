FROM postgres
ENV POSTGRES_PASSWORD DB_password
ENV POSTGRES_DB project
COPY restore.sql /docker-entrypoint-initdb.d/
