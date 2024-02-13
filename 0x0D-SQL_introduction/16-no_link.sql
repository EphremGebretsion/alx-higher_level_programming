-- list all records with name value
-- this command prints all the rows that contain name value from "second_table" table
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
