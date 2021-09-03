FROM mysql:5.7

ADD ../databases/schema/schema.sql /docker-entrypoint-initdb.d

EXPOSE 3306