docker run -d \
  -e MYSQL_ROOT_PASSWORD=pinaxai \
  -e MYSQL_DATABASE=pinaxai \
  -e MYSQL_USER=pinaxai \
  -e MYSQL_PASSWORD=pinaxai \
  -p 3306:3306 \
  -v mysql_data:/var/lib/mysql \
  -v $(pwd)/cookbook/mysql-init:/docker-entrypoint-initdb.d \
  --name mysql \
  mysql:8.0
