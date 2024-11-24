CREATE DATABASE IF NOT EXISTS trash;
USE trash;

/* Table to store raw data from CSV */
CREATE TABLE IF NOT EXISTS bin_locations_raw (
    id INT AUTO_INCREMENT PRIMARY KEY,
    district VARCHAR(255),
    address VARCHAR(255),
    detailed_address VARCHAR(255),
    location_type VARCHAR(255),
    bin_type VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_raw_entry UNIQUE (district, address, detailed_address)
);

LOAD DATA LOCAL INFILE '~/Projects/littering_and_bins/data/seoul_bins.csv'
INTO TABLE bin_locations_raw
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@dummy, district, address, detailed_address, location_type, bin_type)
SET
    district = TRIM(district),
    address = TRIM(address),
    detailed_address = TRIM(detailed_address),
    location_type = TRIM(location_type),
    bin_type = TRIM(bin_type);

/* 
Table for cleaned-up bin locations
No duplicates allowed as bin location is unique
Only address information necessary for analysis is extracted
*/
CREATE TABLE IF NOT EXISTS bin_locations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    district VARCHAR(255),
    address VARCHAR(255),
    latitude DOUBLE,
    longitude DOUBLE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT unique_district_address UNIQUE (district, address)
);

INSERT INTO bin_locations (district, address)
SELECT DISTINCT district, address
FROM bin_locations_raw
ON DUPLICATE KEY UPDATE
    updated_at = CURRENT_TIMESTAMP;


/*
Table for bin locations in selected districts
Only districts with information about illegal dumping are selected
*/
CREATE TABLE IF NOT EXISTS bin_locations_focus AS
SELECT *
FROM bin_locations
WHERE district IN ('용산구', '강남구');

ALTER TABLE bin_locations_focus
ADD CONSTRAINT unique_district_address_focus UNIQUE (district, address);
ADD COLUMN updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

/* 
Ensures no duplicate data even when the same CSV is run multiple times
*/
INSERT INTO bin_locations_focus (district, address, created_at, updated_at)
SELECT bin_locations.district, bin_locations.address, bin_locations.created_at, CURRENT_TIMESTAMP
FROM bin_locations
WHERE bin_locations.district IN ('용산구', '강남구')
  AND NOT EXISTS (
      SELECT 1
      FROM bin_locations_focus
      WHERE bin_locations_focus.district = bin_locations.district
        AND bin_locations_focus.address = bin_locations.address
  )
ON DUPLICATE KEY UPDATE
    updated_at = CURRENT_TIMESTAMP;
