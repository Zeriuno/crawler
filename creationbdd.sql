CREATE DATABASE mimocrawlerdb;
CREATE USER 'mimocrawlerusr'@'localhost' IDENTIFIED BY 'yolo';
GRANT ALL PRIVILEGES ON mimocrawlerdb.* TO 'mimocrawlerusr'@'localhost';
FLUSH PRIVILEGES;

DROP TABLE url;
DROP TABLE words;

CREATE TABLE url(
  id INT AUTO_INCREMENT PRIMARY KEY,
  url VARCHAR(300) NOT NULL,
  date DATE NOT NULL
);

CREATE TABLE words(
  id INT AUTO_INCREMENT PRIMARY KEY,
  url VARCHAR(300) references url(url),
  item VARCHAR(300),
  occurrences INT,
  percentage FLOAT
);
