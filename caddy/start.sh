#!/bin/bash

set -e

if [ -z "$DOMAIN" ]
then
    # If DOMAIN is blank, set to localhost
    # Note: in prod, domain will be the actual domain
    export DOMAIN="ec2-54-183-133-161.us-west-1.compute.amazonaws.com"
fi

caddy run --config /etc/caddy/Caddyfile --adapter caddyfile
