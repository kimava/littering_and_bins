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
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    latitude DOUBLE,
    longitude DOUBLE,
    CONSTRAINT unique_address_district UNIQUE (address, district)
);

LOAD DATA LOCAL INFILE '~/Projects/littering_and_bins/data/raw/yongsangu_dumping.csv'
IGNORE INTO TABLE illegal_littering
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@dummy, @raw_address, @dummy)
SET address = TRIM(@raw_address), 
    district = 'yongsan', 
    create_time = CURRENT_TIMESTAMP;

LOAD DATA LOCAL INFILE '~/Projects/littering_and_bins/data/raw/gangnamgu_dumping.csv'
IGNORE INTO TABLE illegal_littering
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@dummy, @raw_address, @dummy)
SET address = TRIM(@raw_address), 
    district = 'gangnam', 
    create_time = CURRENT_TIMESTAMP;