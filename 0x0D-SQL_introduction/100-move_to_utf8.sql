-- Convert 'hbtn_0c_0' to utf8mb4
-- Convert db 'hbtn_0c_0'
ALTER DATABASE hbtn_0c_0
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;
-- Convert table 'first_table'
ALTER TABLE hbtn_0c_0.first_table
CHARACTER SET = utf8mb4
COLLATE utf8mb4_unicode_ci;
-- Convert field 'name'
ALTER TABLE hbtn_0c_0.first_table
MODIFY 'name' VARCHAR(256)
CHARACTER SET = utf8mb4
COLLATE utf8mb4_unicode_ci;
