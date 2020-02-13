/*
 * Практическое задание теме “Агрегация данных”
 *
 * Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. 
 * Следует учесть, что необходимы дни недели текущего года, а не года рождения.
 */

DROP DATABASE IF EXISTS shop;
CREATE DATABASE shop;
USE shop;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Имя покупателя',
  birthday_at DATE COMMENT 'Дата рождения',
  created_at DATETIME,
  updated_at DATETIME
) COMMENT = 'Покупатели';

INSERT INTO users (name, birthday_at) VALUES
  ('Геннадий', '1990-10-05'),
  ('Геннадий', '1990-10-12'),
  ('Наталья', '1984-11-12'),
  ('Александр', '1985-05-20'),
  ('Александр', '1985-05-27'),
  ('Сергей', '1988-02-14'),
  ('Иван', '1998-01-12'),
  ('Мария', '1992-08-29');

 SELECT
 DATE_FORMAT(STR_TO_DATE(CONCAT_WS('-', SUBSTRING(NOW(), 1, 4), SUBSTRING(birthday_at, 6, 2), SUBSTRING(birthday_at, 9, 2)), '%Y-%m-%d'), '%W') as week_day
 , COUNT(*)
 FROM users
 GROUP BY week_day