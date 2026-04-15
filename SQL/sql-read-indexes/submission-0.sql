CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT
);
-- Do not modify above this line. --

select *
from pg_viewers
where tablename = 'pokemon';



