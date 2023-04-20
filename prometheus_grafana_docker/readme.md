**Simple PING-monitor Prometheus and Docker based project**\
This tool allows monitor host across the network(local or internet) using very popular PING method. Big adventage is you cannot install any agent on
remote host. Only condition is remote site must be able to respond for ping.
Stack: four  containers (Prometheus, Ping Exportedr, Grafana, Alert Manager). 
Ping_Exporter is simple Prometheus exporter (https://github.com/czerwonk/ping_exporter) that ping hosts and gives a few simple metrics like ping best, worst, mean time, standard deviation, lost ping ratio etc.
Metric are collected in Prometheus and visualised in Grafana, so you can check ping statistic in a convinient way in period of time you need.(for example from two days or couple of hours)
Alertmanager send email if some of hosts not responding for ping for about minute(lost ratio growing and finally reach 1 - alert becomes active). Sender and receiver mail adresses can be definied in alertmanager.yaml. By default Alertmanager is configured for gmail, but anty diffrent Alertmaaager receiver can be used.
Ping host list can be definied in  ./ping-exporter/config.yml file. IP and hostname are supprted. By default ipv6 is disabled, DNS server also can be definied.(see config.yml file)

all you need is Docker and Docker composer installed. 

Runing: **go to main project dir, issue command: "sudo docker compose up".**



default host addr:\
Grafana: localhost:3000\
Prometheus: localhost:9090\
Ping Exporter: localhost:9427\
Alertmanager: localhost:9093

ports can be easy modifed in **compose.yaml** 