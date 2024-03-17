-- Database: public

-- DROP DATABASE IF EXISTS public;

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

-- CREATE TABLE customers ();

-- ALTER TABLE customers ADD COLUMN customer_ID SERIAL PRIMARY KEY, ADD COLUMN first_name VARCHAR(50), ADD COLUMN surname VARCHAR(50);


-- INSERT INTO customers (first_name, surname)
-- VALUES ('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson');
-- SELECT * FROM customers WHERE surname = 'Smith';
-- SELECT * FROM customers WHERE surname = 'Jones';
-- SELECT * FROM customers WHERE surname != 'Scott';