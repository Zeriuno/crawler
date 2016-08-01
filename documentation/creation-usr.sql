CREATE DATABASE mimocrawlerdb;
CREATE USER 'mimocrawlerusr'@'localhost' IDENTIFIED BY 'yolo';
GRANT ALL PRIVILEGES ON mimocrawlerdb.* TO 'mimocrawlerusr'@'localhost';
FLUSH PRIVILEGES;
