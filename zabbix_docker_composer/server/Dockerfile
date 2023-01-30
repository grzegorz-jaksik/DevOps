FROM debian:11
RUN apt -y update

#instalujemy WGET
RUN apt -y install wget


#pobieranie i instalacja repozytorium zabbix
RUN wget https://repo.zabbix.com/zabbix/6.2/debian/pool/main/z/zabbix-release/zabbix-release_6.2-4%2Bdebian11_all.deb
RUN dpkg -i zabbix-release_6.2-4+debian11_all.deb
RUN apt update

#instalacja serwera,
RUN apt  -y install zabbix-server-pgsql

#schematy do bazy.
RUN apt  -y install zabbix-sql-scripts

#instalacja klienta postgres
RUN apt -y install postgresql-client


RUN mkdir /var/run/zabbix

#plik logowania
RUN touch /tmp/zabbix_server.log
RUN chown zabbix:zabbix /tmp/zabbix_server.log

#plik konfiguracyjny
COPY --chown=zabbix:zabbix zabbix_server.conf /etc/zabbix/zabbix_server.conf

#zmiana usera
USER zabbix

#uruchomienie serwera
CMD zabbix_server --foreground

EXPOSE 10051