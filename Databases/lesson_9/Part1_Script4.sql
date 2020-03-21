
/*
 * (по желанию) Пусть имеется любая таблица с календарным полем created_at. 
 * Создайте запрос, который удаляет устаревшие записи из таблицы, оставляя только 5 самых свежих записей.
 */


DROP DATABASE IF EXISTS sample3;
CREATE DATABASE sample3;
USE sample3;

DROP TABLE IF EXISTS a_dates;
CREATE TABLE a_dates
(
	a_date DATE
);

INSERT INTO a_dates VALUES
('2016-08-01'),
('2018-08-02'),
('2018-08-03'),
('2012-08-04'),
('2015-08-05'),
('2018-08-06'),
('2018-08-07'),
('2013-08-08');

DELETE a_dates FROM a_dates
JOIN
 	(SELECT a_date FROM a_dates
  	ORDER BY a_date DESC LIMIT 5, 1) AS t
ON a_dates.a_date <= t.a_date;