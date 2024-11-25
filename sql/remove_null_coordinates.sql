/* This script removes rows with NULL latitude or longitude values */

use trash;

/* Delete rows with NULL values in latitude or longitude
from bin_locations_focus */
DELETE FROM bin_locations_focus
WHERE latitude IS NULL OR longitude IS NULL;

/* Delete rows with NULL values in latitude or longitude
from illegal_littering */
DELETE FROM illegal_littering
WHERE latitude IS NULL OR longitude IS NULL;

/* Count the number of rows where latitude or longitude is NULL in each table */
SELECT 'bin_locations_focus' AS table_name,
        COUNT(*) AS null_rows_with_lat_lng
FROM bin_locations_focus
WHERE latitude IS NULL
    OR longitude IS NULL
UNION
SELECT 'illegal_littering',
        COUNT(*) AS null_rows_with_lat_lng
FROM illegal_littering
WHERE latitude IS NULL
    OR longitude IS NULL;