-- -- Database: public

-- -- DROP DATABASE IF EXISTS public;

-- CREATE DATABASE public
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United Kingdom.1252'
--     LC_CTYPE = 'English_United Kingdom.1252'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- CREATE TABLE items ()
-- ALTER TABLE items ADD COLUMN item_ID SERIAL PRIMARY KEY, ADD COLUMN item_name VARCHAR(50), ADD COLUMN item_price MONEY;

-- INSERT INTO items (item_name, item_price)
-- VALUES ('Small desk', 100), ('Large desk', 300), ('Fan', 80);

-- SELECT * FROM items;
-- ALTER TABLE items ALTER COLUMN item_price SET DATA TYPE decimal;
-- SELECT * FROM items WHERE item_price > 80;
-- SELECT * FROM items WHERE item_price <= 300;
