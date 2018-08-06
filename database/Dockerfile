FROM mysql:5.6.41
MAINTAINER Jack Malashchytski <hustlequeen@mail.ru>

ENV SECRETS_PATH /run/secrets

ENV MYSQL_ROOT_PASSWORD_FILE $SECRETS_PATH/mysql-root-password
ENV MYSQL_DATABASE_FILE      $SECRETS_PATH/mysql-database
ENV MYSQL_USER_FILE          $SECRETS_PATH/mysql-user
ENV MYSQL_PASSWORD_FILE      $SECRETS_PATH/mysql-password

COPY ./secrets $SECRETS_PATH/

COPY ./scripts /docker-entrypoint-initdb.d/

RUN mkdir -p /var/lib/mysql
VOLUME /var/lib/mysql

EXPOSE 3306