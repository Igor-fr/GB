/*
 * Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.
 */

SELECT name FROM users WHERE id in (SELECT user_id FROM orders);