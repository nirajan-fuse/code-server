#!/bin/sh

sh /tmp/20-envsubst-on-templates.sh

sudo nginx -g 'daemon off;'

sh service nginx reload
