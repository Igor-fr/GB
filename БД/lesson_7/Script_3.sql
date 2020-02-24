/*
 * (по желанию) Пусть имеется таблица рейсов flights (id, from, to) и 
 * таблица городов cities (label, name). Поля from, to и label содержат
 * английские названия городов, поле name — русское. Выведите список 
 * рейсов flights с русскими названиями городов.
 */

SELECT c1.name, c2.name
FROM flights
     JOIN cities c1 ON flights.from = c1.label
     JOIN cities c2 ON flights.to = c2.label
ORDER BY flights.id
 