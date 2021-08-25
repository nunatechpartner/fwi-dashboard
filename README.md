# fwi-dashboard
Superset dashboard for FWI kpis viz

### Installation process
```
# Start Redis & MySQL services
docker-compose up -d redis mysql
# Wait for services to come up fully...

# Start Superset
docker-compose up -d superset
# Wait for Superset to come up fully...

# Initialize Superset DB
docker-compose exec superset superset-init
# and fill with super user data needed

# This link to follow nginx with http and https and autorenewal certificates
https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71

chmod +x init-letsencrypt.sh
sudo ./init-letsencrypt.sh
# If needed fill with info

# Everything down
docker-compose stop && docker system prune -f

# Everything up ready for prod
docker-compose up -d

```
