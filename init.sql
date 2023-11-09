-- init.sql
CREATE USER 'microblog-DB_USER'@'%' IDENTIFIED BY 'dettaervoratpw';
GRANT ALL PRIVILEGES ON `microblog-db`.* TO 'microblog-DB_USER'@'%';
FLUSH PRIVILEGES;

