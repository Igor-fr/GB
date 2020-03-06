/*
 * Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. 
 * С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", 
 * с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", 
 * с 18:00 до 00:00 — "Добрый вечер", 
 * с 00:00 до 6:00 — "Доброй ночи".
 */

DROP FUNCTION IF EXISTS MESSAGE;
DELIMITER $$
CREATE FUNCTION MESSAGE() RETURNS CHAR(255) DETERMINISTIC
BEGIN
	DECLARE h INT DEFAULT HOUR(NOW());
	DECLARE msg CHAR(255) DEFAULT '';
	CASE
		WHEN h >= 6 and h < 12 THEN SET msg = "Доброе утро!";
		WHEN h >= 12 and h < 18 THEN SET msg = "Добрый день!";
		WHEN h >= 18 and h < 24 THEN SET msg = "Добрый вечер!";
		WHEN h >= 0 and h < 6 THEN SET msg = "Доброй ночи!";
	END CASE;
	RETURN msg;
END $$
DELIMITER ;

SELECT MESSAGE();