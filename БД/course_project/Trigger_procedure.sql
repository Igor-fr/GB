/*
 * (Триггер) При попытке включения или изменения в заказанных товарах количества какого-либо товара больше, чем его есть в наличии, выдавать ошибку. 
 */

DROP TRIGGER IF EXISTS t_count_ins;
DROP TRIGGER IF EXISTS t_count_upd;
DROP PROCEDURE IF EXISTS p_customer_orders;

DELIMITER $$
CREATE TRIGGER t_count_ins BEFORE INSERT ON ordered_products
FOR EACH ROW 
BEGIN
	DECLARE cnt_ INT;
	SELECT vp.stock INTO cnt_ FROM v_prod vp WHERE vp.id = NEW.product_id;
	IF (NEW.count_product > cnt_) THEN 
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = "Товара недостаточно!";
	END IF;
END $$


CREATE TRIGGER t_count_upd BEFORE UPDATE ON ordered_products
FOR EACH ROW 
BEGIN
	DECLARE cnt_ INT;
	SELECT vp.stock INTO cnt_ FROM v_prod vp WHERE vp.id = OLD.product_id;
	IF (NEW.count_product - OLD.count_product > cnt_) THEN 
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = "Товара недостаточно!";
	END IF;
END $$


/*
 * (Процедура) По email пользователя вывести номера всех его заказов, названия товаров и каталогов, 
 * их количество, а также информацию о доставке и оплате.
 */

CREATE PROCEDURE p_customer_orders(IN email VARCHAR(50)) NOT DETERMINISTIC
BEGIN
	DECLARE id_ INT;
	SELECT id INTO id_ FROM customers c WHERE c.email = email;
	SELECT o.id as order_number, p.name as product, c.name as catalog_name, op.count_product as count_prod, so.paid as paid, so.deliver as delivered
	FROM orders o JOIN ordered_products op ON o.id = op.order_id
				  JOIN products p ON op.product_id = p.id 
				  JOIN catalogs c ON p.catalog_id = c.id
				  JOIN status_order so ON o.id = so.order_id 
	WHERE o.customer_id = id_;
END $$
DELIMITER ;

CALL p_customer_orders('hagenes.erin@example.com');
