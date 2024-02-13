-- converts the database to UTF8
-- this command will change database hbtn_0v_0 to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- table to utf-8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;
-- data field to utf-8
ALTER TABLE first_table
MODIFY name VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_unicode_ci;
