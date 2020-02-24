DROP DATABASE IF EXISTS airoport;
CREATE DATABASE airoport;
USE airoport;

DROP TABLE IF EXISTS flights;
CREATE TABLE flights (
  id SERIAL PRIMARY KEY,
  `from` VARCHAR(255),
  `to` VARCHAR(255)
);

DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
  label VARCHAR(255),
  name VARCHAR(255)
);

INSERT INTO flights VALUES
  ('1', 'moscow', 'omsk'),
  ('2', 'novgorod', 'kazan'),
  ('3', 'irkutsk', 'moscow'),
  ('4', 'omsk', 'irkutsk'),
  ('5', 'moscow', 'kazan');
  
 INSERT INTO cities VALUES
  ('moscow', 'Москва'),
  ('irkutsk', 'Иркутск'),
  ('novgorod', 'Новгород'),
  ('kazan', 'Казань'),
  ('omsk', 'Омск');