/*
 * Получить список из 5 самых дорогих товаров, указать имя товара, имя каталога и стоимость товара.
 */

SELECT p.name as product_name, c.name as catalog_name, coast as coast 
FROM products p JOIN catalogs c ON p.catalog_id = c.id 
ORDER BY coast DESC LIMIT 5;


/*
 * Показать последние 10 заказов, с указанием номера заказа, ФИО продавца и покупателя, а также почтового адреса покупателя.
 */

SELECT o.id as order_number, CONCAT(s.firstname, ' ', s.lastname) as seller, CONCAT(c.firstname, ' ', c.lastname) as customer, c.email as email_customer
FROM orders o JOIN sellers s ON o.seller_id = s.id 
			  JOIN customers c ON o.customer_id = c.id 
ORDER BY o.date_order DESC LIMIT 10;


/*
 * Вывести товары, купленные в текущем году, с указанием их номера заказа, названия товара и соответствующего каталога, 
 * упорядочив по убыванию количества купленных позиций.
 */

SELECT o.id as order_number, p.name as product_name, c.name as catalog_name, op.count_product as count_product, o.date_order as date_order
FROM ordered_products op JOIN products p ON op.product_id = p.id 
						 JOIN catalogs c ON p.catalog_id = c.id 
						 JOIN orders o ON op.order_id = o.id 
						 WHERE YEAR(o.date_order) = YEAR(NOW())
ORDER BY op.count_product DESC;


/*
 * Вывести все заказы, с указанием количества товарных позиций в каждом заказе.
 */

SELECT op.order_id, count(*) FROM ordered_products op GROUP BY op.order_id;
