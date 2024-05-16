FROM caddy/caddy:2.7.6-alpine

RUN mkdir /app
COPY start.sh /app/start.sh

COPY Caddyfile /etc/caddy/Caddyfile
RUN apk add  --no-cache nss-tools

CMD ["sh", "/app/start.sh"]
