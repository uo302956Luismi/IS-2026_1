docker run --rm -d --network pruebas --name nginx \
       -v $(pwd)/html:/usr/share/nginx/html -p 80:80 \
       -v $(pwd)/sitios_nginx:/etc/nginx/conf.d nginx