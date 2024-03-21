-- Database: RestaurantMenuManager

-- DROP DATABASE IF EXISTS "RestaurantMenuManager";

-- CREATE DATABASE "RestaurantMenuManager"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United Kingdom.1252'
--     LC_CTYPE = 'English_United Kingdom.1252'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- CREATE TABLE Menu_Items (
-- item_id SERIAL PRIMARY KEY,
-- item_name VARCHAR(30) NOT NULL,
-- item_price SMALLINT DEFAULT 0
-- )

-- INSERT INTO Menu_Items (item_name, item_price) VALUES
-- ('Hamburger', 10), ('Falafel', 7);

SELECT * FROM Menu_Items;