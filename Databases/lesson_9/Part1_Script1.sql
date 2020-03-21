/*
 * В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. 
 * Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте транзакции.
 */

START TRANSACTION;

INSERT INTO sample.users (name, birthday_at, created_at, updated_at) SELECT (name), (birthday_at), (created_at), (updated_at) FROM users WHERE users.id = 1;

COMMIT;

