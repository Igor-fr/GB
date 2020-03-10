DROP DATABASE IF EXISTS store;

CREATE DATABASE store;
USE store;


DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
	id SERIAL PRIMARY KEY,
   	name VARCHAR(50) NOT NULL,
    INDEX catalog_idx(name)
);

DROP TABLE IF EXISTS products;
CREATE TABLE products (
	id SERIAL PRIMARY KEY,
   	name VARCHAR(50) NOT NULL,
    catalog_id BIGINT UNSIGNED NOT NULL,
    coast INT NOT NULL,
    INDEX catalog_idx(catalog_id),
    INDEX name_idx(name),
    FOREIGN KEY (catalog_id) REFERENCES catalogs(id)
);

DROP TABLE IF EXISTS suppliers;
CREATE TABLE suppliers (
	id SERIAL PRIMARY KEY,
   	address VARCHAR(50) NOT NULL,
   	firstname VARCHAR(50) NOT NULL,
   	lastname VARCHAR(50) NOT NULL,
    INDEX name_idx(firstname, lastname)
);

DROP TABLE IF EXISTS supply;
CREATE TABLE supply (
	id SERIAL PRIMARY KEY,
   	supplier_id BIGINT UNSIGNED NOT NULL,
    date_supply DATETIME DEFAULT NOW(),
    INDEX supply_idx(id),
    INDEX supplier_idx(supplier_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

DROP TABLE IF EXISTS supplied_products;
CREATE TABLE supplied_products (
	supply_id BIGINT UNSIGNED NOT NULL,
   	product_id BIGINT UNSIGNED NOT NULL,
    count_product INT UNSIGNED NOT NULL,
    INDEX supply_idx(supply_id),
    INDEX supplier_idx(product_id),
    FOREIGN KEY (supply_id) REFERENCES supply(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    PRIMARY KEY (supply_id, product_id)
);

DROP TABLE IF EXISTS sellers;
CREATE TABLE sellers (
	id SERIAL PRIMARY KEY,
   	firstname VARCHAR(50) NOT NULL,
   	lastname VARCHAR(50) NOT NULL,
   	date_employment DATETIME DEFAULT NOW(),
    INDEX name_idx(firstname, lastname)
);

DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
   	firstname VARCHAR(50) NOT NULL,
   	lastname VARCHAR(50) NOT NULL,
   	email VARCHAR(50) NOT NULL UNIQUE,
   	phone BIGINT NOT NULL,
   	address VARCHAR(50) NOT NULL,
   	date_registration DATETIME DEFAULT NOW(),
    INDEX name_idx(firstname, lastname)
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
	id SERIAL PRIMARY KEY,
   	seller_id BIGINT UNSIGNED NOT NULL,
    customer_id BIGINT UNSIGNED NOT NULL,
    date_order DATETIME DEFAULT NOW(),
    INDEX seller_idx(seller_id),
    INDEX customer_idx(customer_id),
    FOREIGN KEY (seller_id) REFERENCES sellers(id),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

DROP TABLE IF EXISTS ordered_products;
CREATE TABLE ordered_products (
	order_id BIGINT UNSIGNED NOT NULL,
   	product_id BIGINT UNSIGNED NOT NULL,
    count_product INT UNSIGNED NOT NULL,
    INDEX supply_idx(order_id),
    INDEX supplier_idx(product_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    PRIMARY KEY (order_id, product_id)
);

DROP TABLE IF EXISTS status_order;
CREATE TABLE status_order (
	order_id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
   	paid BOOL DEFAULT FALSE,
    deliver BOOL DEFAULT FALSE,
    INDEX supply_idx(order_id),
    FOREIGN KEY (order_id) REFERENCES orders(id)
);