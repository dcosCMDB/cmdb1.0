docker run --restart=always --name cmdb-mysql -p 3306:3306 -v /etc/my.cnf:/etc/mysql/mysql.conf.d/mysqld.cnf -v /data/mysql:/var/lib/mysql -e MYSQL\_ROOT\_PASSWORD=root -d mysql
