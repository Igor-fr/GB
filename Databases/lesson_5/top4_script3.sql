/*
 * Практическое задание теме “Агрегация данных”
 *
 * Подсчитайте произведение чисел в столбце таблицы
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
  
 SELECT ROUND(EXP(SUM(LN(id)))) FROM users;