USE mimocrawlerdb;
DROP TABLE IF EXISTS url, words, links;

CREATE TABLE url(
  idurl INT AUTO_INCREMENT PRIMARY KEY,
  url VARCHAR(300) NOT NULL,
  date DATETIME NOT NULL
);

CREATE TABLE words(
  idword INT AUTO_INCREMENT PRIMARY KEY,
  idurl INT references url(idurl),
  item VARCHAR(300) NOT NULL,
  occurrences INT NOT NULL,
  percentage FLOAT
);

CREATE TABLE follow(
  idfollow INT AUTO_INCREMENT PRIMARY KEY,
  link VARCHAR(300) NOT NULL,
  idurl INT references url(idurl), --nécessaire car des fois on a des liens sans mots
  idword INT references words(idword),
  occurrencesfollow INT,
  percentagefollow FLOAT
)
