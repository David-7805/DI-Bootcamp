-- Database: DailyChallengeWeek3Day3

-- DROP DATABASE IF EXISTS "DailyChallengeWeek3Day3";

-- CREATE DATABASE "DailyChallengeWeek3Day3"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United Kingdom.1252'
--     LC_CTYPE = 'English_United Kingdom.1252'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- Part I
-- 1.
-- CREATE TABLE Customer (
-- id SERIAL PRIMARY KEY,
-- first_name VARCHAR (50),
-- last_name VARCHAR (100) NOT NULL
-- );

-- CREATE TABLE Customer_profile (
-- id SERIAL PRIMARY KEY,
-- isLoggedIn BOOLEAN DEFAULT FALSE,
-- customer_id INT,
-- CONSTRAINT customer_to_profile FOREIGN KEY (customer_id) REFERENCES Customer (id)
-- );

-- 2.
-- INSERT INTO Customer (first_name, last_name) VALUES
-- ('John', 'Doe'), ('Jerome', 'Lalu'), ('Lea', 'Rive');

-- 3.
-- INSERT INTO Customer_profile (isLoggedIn, customer_id) VALUES
-- (TRUE, (SELECT id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe'));
-- INSERT INTO Customer_profile (customer_id) VALUES
-- ((SELECT id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

-- 4.
-- SELECT Customer.first_name FROM Customer JOIN Customer_profile
-- ON Customer.id = Customer_profile.customer_id
-- WHERE Customer_profile.isLoggedIn = TRUE;

-- SELECT Customer.first_name, Customer_profile.isLoggedIn FROM Customer
-- LEFT OUTER JOIN Customer_profile ON Customer.id = Customer_profile.customer_id;

-- SELECT COUNT(*) FROM Customer LEFT OUTER JOIN Customer_profile ON Customer.id = Customer_profile.customer_id
-- WHERE Customer_profile.isLoggedIn = FALSE OR Customer_profile.isLoggedIn IS NULL;

-- Part II
-- 1.
-- CREATE TABLE Book (
-- book_id SERIAL PRIMARY KEY,
-- title VARCHAR (100) NOT NULL,
-- author VARCHAR (100) NOT NULL
-- );

-- 2.
-- INSERT INTO Book (title, author) VALUES
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To kill a mockingbird', 'Harper Lee');

-- 3.
-- CREATE TABLE Student (
-- student_id SERIAL PRIMARY KEY,
-- name VARCHAR (100) NOT NULL UNIQUE,
-- age SMALLINT NOT NULL,
-- CHECK (age <= 15)
-- )

-- 4.
-- INSERT INTO Student (name, age) VALUES
-- ('John', 12), ('Lera', 11), ('Patrick', 10), ('Bob', 14);

-- 5.
-- CREATE TABLE Library (
-- book_fk_id SMALLINT NOT NULL,
-- student_id SMALLINT NOT NULL,
-- borrowed_date DATE,
-- PRIMARY KEY (book_fk_id, student_id),
-- FOREIGN KEY (book_fk_id) REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
-- );

-- 6.
-- INSERT INTO Library (book_fk_id, student_id, borrowed_date) VALUES
-- ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
--  (SELECT student_id FROM Student WHERE name = 'John'), '15/02/2022');

-- INSERT INTO Library (book_fk_id, student_id, borrowed_date) VALUES
-- ((SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'),
-- (SELECT student_id FROM Student WHERE name = 'Bob'), '03/03/2021');

-- INSERT INTO Library (book_fk_id, student_id, borrowed_date) VALUES
-- ((SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
-- (SELECT student_id FROM Student WHERE name = 'Lera'), '23/05/2021');

-- INSERT INTO Library (book_fk_id, student_id, borrowed_date) VALUES
-- ((SELECT book_id FROM Book WHERE title = 'Harry Potter'),
-- (SELECT student_id FROM Student WHERE name = 'Bob'), '12/08/2021');

--  7.
-- SELECT * FROM Library;

-- SELECT Student.name, Book.title FROM Student JOIN Library ON Student.student_id = Library.student_id
-- JOIN Book ON Library.book_fk_id = Book.book_id;

-- SELECT AVG(Student.age) FROM Student JOIN Library ON Student.student_id = Library.student_id
-- JOIN Book ON Library.book_fk_id = Book.book_id WHERE Book.title = 'Alice In Wonderland';

-- DELETE FROM Student WHERE name = 'John';
-- SELECT * FROM Library;
-- After deleting John, the (only) row in Library that contained data about him was deleted as well.