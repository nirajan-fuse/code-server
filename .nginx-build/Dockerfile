FROM nginx:1.27-alpine

# COPY ./nginx_config /etc/nginx/conf.d/

COPY ./nginx.conf.template /etc/nginx/templates/default.conf.template

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]