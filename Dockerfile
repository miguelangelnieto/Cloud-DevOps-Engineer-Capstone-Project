FROM nginx

COPY ./posts/ /usr/share/nginx/html/

EXPOSE 80