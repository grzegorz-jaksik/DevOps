Simple PING-monitor Prometheus and Docker based project.
This tool set allows monitor and detect host across the network(local or internet) using very popular PING method.
It Contains three  containers (Prometheus, Ping Exportedr, Grafana). 
Ping_Exporter is simple Prometheus exporter (https://github.com/czerwonk/ping_exporter) witch ping hosts and gives a few simple metrics like ping best, worst, mean time, standard deviation, lost ping ratio etc.
Metric are collected in Prometheus and visualised in Grafana, so you can check ping statistic in a convinient way in a period of time you need.(for example from two days or couple of hours)
Host can be definied in  ./ping-exporter/config.yml file. IP and hostname are supprted. By default ipv6 is disabled, DNS server also can be definied.(see config.yml file)
all you need is Docker and Docker composer installed. 

Runing  command: "sudo docker compose up" in main project directory. 

default host addr:
Grafana: localhost:3000
Prometheus: localhost:9090
Ping Exporter: localhost:9427

above settings can be easy modifed in compose.yaml 