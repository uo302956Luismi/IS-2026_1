docker run --rm -d --network pruebas    --name nginx -p 80:80    -v /home/uo302956/IS-2026/html:/usr/share/nginx/html    -v /home/uo302956/IS-2026/sitios_nginx:/etc/nginx/conf.d nginx
