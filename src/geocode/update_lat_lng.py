from geopy.geocoders import Nominatim
from src.db.db_connector import create_connection
import re

geolocator = Nominatim(user_agent="littering_and_bins")

def clean_address(address):
    address = re.sub(r"^\s*\S*동\s*", "", address)
    address = re.sub(r"\s*\(.*?\)", "", address)
    address = address.replace(" ", "")
    return address

def update_coordinates(batch_size=300):
    db = create_connection()
    cursor = db.cursor()

    try:
        cursor.execute("SELECT id, address FROM bin_locations_focus WHERE latitude IS NULL OR longitude IS NULL")
        rows = cursor.fetchall()

        for row in rows:
            entry_id, address = row
            location = geolocator.geocode(address, timeout=10)

            if location:
                latitude = location.latitude
                longitude = location.longitude

                cursor.execute(
                    "UPDATE bin_locations_focus SET latitude = %s, longitude = %s WHERE id = %s",
                    (latitude, longitude, entry_id)
                )
                print("done")
            else:
                print(f"Address not found: {address}")

        db.commit()

        offset = 0
        while True:
            print(f"Processing batch starting at offset {offset}")
            cursor.execute(f"""
                SELECT id, address 
                FROM illegal_littering 
                WHERE latitude IS NULL OR longitude IS NULL 
                LIMIT {batch_size} OFFSET {offset}
            """)
            rows = cursor.fetchall()

            if not rows:
                break

            for row in rows:
                entry_id, address = row
                cleaned_address = clean_address(address)
                location = geolocator.geocode(cleaned_address, timeout=10)

                if location:
                    latitude = location.latitude
                    longitude = location.longitude

                    cursor.execute(
                        """
                        UPDATE illegal_littering 
                        SET latitude = %s, longitude = %s
                        WHERE id = %s
                        """,
                        (latitude, longitude, entry_id)
                    )
                    print(f"Updated {entry_id}")
                else:
                    print(f"Address not found: {cleaned_address}")
                
            db.commit()
            offset += batch_size

    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()

    finally:
        cursor.close()
        db.close() 

update_coordinates()
