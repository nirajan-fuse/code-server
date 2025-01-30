#!/bin/sh

NOTEBOOK_USER=${NOTEBOOK_USER}
sudo sed -i "s|\${NOTEBOOK_USER}|${NOTEBOOK_USER}|g" /tmp/login-with-args.html

sh /tmp/20-envsubst-on-templates.sh

sudo nginx -g 'daemon off;'

sh service nginx reload
