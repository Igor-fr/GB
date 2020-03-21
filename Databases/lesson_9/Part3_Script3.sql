/*
 * (по желанию) Напишите хранимую функцию для вычисления произвольного числа Фибоначчи. 
 * Числами Фибоначчи называется последовательность в которой число равно сумме двух предыдущих чисел. 
 * Вызов функции FIBONACCI(10) должен возвращать число 55.
*/

DROP FUNCTION IF EXISTS FIBONACCI;
DELIMITER $$
CREATE FUNCTION FIBONACCI(cnt INT) RETURNS INT DETERMINISTIC
BEGIN
	DECLARE temp1 INT DEFAULT 0;
	DECLARE temp2 INT DEFAULT 1;
	DECLARE temp3 INT DEFAULT 0;
	IF cnt = 1 THEN
		SET temp3 = 1;
	END IF;
	WHILE cnt > 1 DO
		SET temp3 = temp1 + temp2;
		SET temp1 = temp2;
		SET temp2 = temp3;
		SET cnt = cnt - 1;
	END WHILE;
	RETURN temp3;
END $$
DELIMITER ;

SELECT FIBONACCI(10);
