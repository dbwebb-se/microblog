# Monitoring (kmom04)

Configuration for Prometheus, Alertmanager and Grafana. It is used in kmom04 and runs locally with docker compose, on top of your own `docker-compose.yml` (it needs a service named `prod`):

```
docker compose -f docker-compose.yml -f monitoring/docker-compose.yml up -d prod prometheus alertmanager grafana
```

- Prometheus: <http://localhost:9090>
- Alertmanager: <http://localhost:9093>
- Grafana: <http://localhost:3000> (`admin` / `admin`)

Put your own URL from <https://webhook.site> in `alertmanager.yml`. Instructions are in the course material for kmom04.
