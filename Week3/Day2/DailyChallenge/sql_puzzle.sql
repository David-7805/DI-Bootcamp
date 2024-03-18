-- -- Database: SQLPuzzle

-- -- DROP DATABASE IF EXISTS "SQLPuzzle";

-- CREATE DATABASE "SQLPuzzle"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United Kingdom.1252'
--     LC_CTYPE = 'English_United Kingdom.1252'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')

-- SELECT * FROM FirstTab

-- CREATE TABLE SecondTab (
--     id integer 
-- )

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)


-- SELECT * FROM SecondTab;

-- Q1. I expected 3 as output, because <SELECT id FROM SecondTab WHERE id IS NULL> is a column of one [null] value,
-- so at least 3 ft.id are NOT IN there. However, the answer is 0.
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );

-- Q2. I expected 2, because 6 and 7 are for sure not in <SELECT id FROM SecondTab WHERE id = 5>,
-- the [null] value is also not in there, but I think it will be skipped.
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );

-- Q3. Here too, I expected 2, because 6 and 7 are for sure not in <SELECT id FROM SecondTab>,
-- and the [null] value will be skipped. However, the answer is 0.
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab );

-- Q4 Here too, I expected 2, because <SELECT id FROM SecondTab WHERE id IS NOT NULL>
-- is the same as <SELECT id FROM SecondTab WHERE id = 5>, because IS NOT NULL is a valid
-- statement in SQL. It is NOT IN ([Null], ...) that seems to cause a problem.
-- SELECT COUNT(*) 
-- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )



