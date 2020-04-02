FROM nginx

COPY ./posts/index.html /usr/share/nginx/html

EXPOSE 80