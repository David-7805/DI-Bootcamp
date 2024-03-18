-- During class in the morning:

-- create table actors(
-- actor_id serial primary key,
-- first_name varchar (50) not null,
-- last_name varchar (100) not null,
-- age date not null,
-- number_oscars smallint not null
-- )

-- insert into actors (first_name, last_name, age, number_oscars)
-- values ('Matt', 'Damon', '08/10/1970', 5),
-- ('George','Clooney','06/05/1961', 2)
-- insert into actors (first_name, last_name, age, number_oscars)
-- values ('Sandra', 'Bullock', '26/07/1964', 1), ('Penelope', 'Cruz', '28/04/1974', 1)
-- delete from actors where actor_id = 1 returning *
-- alter table actors rename column number_oscars to oscars
-- alter table actors drop column age
-- alter table actors add column birthday date
-- update actors set birthday = '01-01-1970' where first_name = 'George'
-- UPDATE actors SET first_name = 'Pennie' WHERE last_name = 'Cruz';
-- UPDATE actors SET oscars = 4 WHERE first_name = 'George' RETURNING *;
-- ALTER TABLE actors RENAME COLUMN birthday TO birthdate;
-- DELETE FROM actors WHERE actor_id = 4 RETURNING first_name, last_name, oscars;


-- Daily Challenge: Actors

-- select COUNT(actor_id) from actors;
-- SELECT * FROM actors;

-- INSERT INTO actors (first_name, last_name, oscars)
-- VALUES ('Penelope', 'Cruz',  1, '28/04/1974'); 'Gives the ERROR: INSERT has more expressions than target columns'

-- INSERT INTO actors (first_name, last_name, oscars, birthdate)
-- VALUES ('Penelope', 'Cruz', 1); 'Gives the ERROR: INSERT has more target columns than expressions'

-- INSERT INTO actors (first_name, last_name, oscars)
-- VALUES ('Penelope', 'Cruz', 1); 'Gives no error, because column birthdate accepts null values after it was dropped and then added again.'

-- INSERT INTO actors (last_name, oscars, birthdate)
-- VALUES ('Damon', 5, '08/10/1970'); 'Gives the ERROR: null value in column "first_name" of relation "actors" violates not-null constraint'


