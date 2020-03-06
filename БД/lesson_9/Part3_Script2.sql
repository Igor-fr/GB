/*
 * В таблице products есть два текстовых поля: name с названием товара и description с его описанием. 
 * Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. 
 * Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены. 
 * При попытке присвоить полям NULL-значение необходимо отменить операцию.
 */


DROP TRIGGER IF EXISTS t_products_ins;
DROP TRIGGER IF EXISTS t_products_upd;

DELIMITER $$
CREATE TRIGGER t_products_ins BEFORE INSERT ON products
FOR EACH ROW
BEGIN
	IF (NEW.name IS NULL and NEW.description IS NULL) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = "Оба поля не могут быть NULL!";
	END IF;
END $$

CREATE TRIGGER t_products_upd BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
	IF (NEW.name IS NULL and NEW.description IS NULL) THEN
		SET NEW.name = OLD.name;
		SET NEW.description = OLD.description;
	END IF;
END $$
DELIMITER ;