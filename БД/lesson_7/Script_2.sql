/*
 * Выведите список товаров products и разделов catalogs, который соответствует товару.
 */

SELECT products.name, catalogs.name
FROM products, catalogs
WHERE products.catalog_id = catalogs.id
