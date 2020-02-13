
/*
Практическое задание по теме “Операторы, фильтрация, сортировка и ограничение”

Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы 
типом VARCHAR и в них долгое время помещались значения в формате "20.10.2017 8:10". 
Необходимо преобразовать поля к типу DATETIME, сохранив введеные ранее значения.
 */

DROP DATABASE IF EXISTS shop;
CREATE DATABASE shop;
USE shop;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Имя покупателя',
  birthday_at DATE COMMENT 'Дата рождения',
  created_at VARCHAR(255),
  updated_at VARCHAR(255)
) COMMENT = 'Покупатели';

INSERT INTO users (name, birthday_at, created_at, updated_at) VALUES
  ('Геннадий', '1990-10-05', '20.10.2017 8:10', '20.10.2018 8:10' ),
  ('Наталья', '1984-11-12', '20.11.2017 8:10', '30.10.2017 8:10'),
  ('Александр', '1985-05-20', '13.10.2017 8:10', '14.10.2017 8:10');
  
 UPDATE users SET 	updated_at = STR_TO_DATE(updated_at , '%d.%m.%Y %k:%i'),
 					created_at = STR_TO_DATE(created_at , '%d.%m.%Y %k:%i');
 					
ALTER TABLE users CHANGE updated_at updated_at DATETIME;
ALTER TABLE users CHANGE created_at created_at DATETIME;