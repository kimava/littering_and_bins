CREATE DATABASE IF NOT EXISTS trash;
USE trash;

/*
Table for storing illegal littering data
The table stores addresses where illegal dumping occurs, categorised by district
Data from public sources will be combined into a single table by district.
*/

CREATE TABLE IF NOT EXISTS illegal_littering (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    district VARCHAR(255),
    address VARCHAR(255),
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

/* 
Clear existing data in the table before inserting new records
[FIX ME]
The reason for TRUNCATING is to avoid duplicate records from previous insertions,
while still preserving data within the original files, which may have internal duplicates.
However, further study is required to find a better solution
that can handle internal duplicates in the source files while maintaining efficient imports.
 */
TRUNCATE TABLE illegal_littering;


/*
No de-duplication
because tracking duplicate occurrences of illegal dumping is important
for identifying frequently affected areas.
*/
LOAD DATA LOCAL INFILE '~/Projects/littering_and_bins/data/yongsangu_dumping.csv'
INTO TABLE illegal_littering
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@dummy, @raw_address, @dummy)
SET address = TRIM(@raw_address), 
    district = 'yongsan', 
    create_time = CURRENT_TIMESTAMP;

LOAD DATA LOCAL INFILE '~/Projects/littering_and_bins/data/gangnamgu_dumping.csv'
INTO TABLE illegal_littering
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@dummy, @raw_address, @dummy)
SET address = TRIM(@raw_address), 
    district = 'gangnam', 
    create_time = CURRENT_TIMESTAMP;