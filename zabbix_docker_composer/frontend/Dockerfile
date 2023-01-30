#obraz
FROM php:7.4-apache
RUN apt update

#kopiowanie zawartości strony
COPY site/zabbix-6.2.6/ui /var/www/html

#instalacja edytora nano
RUN apt-get -y install nano 

#instalacja dodatków do PHP
ADD https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions /usr/local/bin/
RUN chmod +x /usr/local/bin/install-php-extensions && \
    install-php-extensions gd bcmath sockets pdo pdo_pgsql pgsql
RUN apt -y update

#instalacja języków
RUN apt -y install locales

#dodawanie en_US do pliku locale.gen
RUN echo "en_US.UTF-8 UTF-8" >>/etc/locale.gen
RUN locale-gen

#kopiowanie konfigu zabbix-frontend
COPY zabbix.conf.php /var/www/html/conf

EXPOSE 80