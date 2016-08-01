```
CREATE TABLE url(
  id INT NOT NULL AUTO_INCREMENT,
  url VARCHAR(300) NOT NULL,
  date
  PRIMARY KEY (id)
);

CREATE TABLE words(
  url VARCHAR(300) references url(url),
  item VARCHAR(300),
  occurrences INT,
  percentage FLOAT
)
```

La requête pour obtenir les mots d'une page est

SELECT item, occurrences, percentage
FROM  words
WHERE url = $item ;
