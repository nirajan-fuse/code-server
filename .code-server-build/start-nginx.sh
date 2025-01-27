#!/bin/sh

LAB_USER=${LAB_USER}
sudo sed -i "s|\${LAB_USER}|${LAB_USER}|g" /tmp/login-with-args.html

sh /tmp/20-envsubst-on-templates.sh

sudo nginx -g 'daemon off;'

sh service nginx reload
