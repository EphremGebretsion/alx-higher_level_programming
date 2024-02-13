-- this script will creates a table and insert some datas
-- this command will create a table
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
-- this command will adds some rows of data
INSERT INTO second_table(id, name, score) VALUES (1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8);
