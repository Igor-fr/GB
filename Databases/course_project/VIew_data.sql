/*
 * Весь товар на складе с указанием его названия, каталога и актуального количества.
 */

DROP VIEW IF EXISTS v_prod;
CREATE VIEW v_prod AS

SELECT p.id, p.name as product, c.name as catalog_name, t3.stock as stock FROM 
	(SELECT t1.prod as prod_id, SUM(s1 - s2) as stock FROM
		(SELECT sp.product_id as prod, SUM(sp.count_product) as s1 FROM supplied_products sp GROUP BY sp.product_id) as t1
			JOIN
		(SELECT op.product_id as prod, SUM(op.count_product) as s2 FROM ordered_products op GROUP BY op.product_id) as t2
			ON t1.prod = t2.prod
	GROUP BY t1.prod) as t3
JOIN products p ON t3.prod_id = p.id 
JOIN catalogs c ON p.catalog_id = c.id;


/*
 * Список неоплаченных заказов с указанием номера заказа, ФИО, почта и телефон должника и даты, когда заказ был составлен.
 */

DROP VIEW IF EXISTS v_paid;
CREATE VIEW v_paid AS 

SELECT o.id as order_number, CONCAT(c.firstname, ' ', c.lastname) as customer, c.email as email, c.phone as phone, o.date_order as date_order
FROM status_order so JOIN orders o ON so.order_id = o.id 
					 JOIN customers c ON o.customer_id = c.id
WHERE paid = FALSE;